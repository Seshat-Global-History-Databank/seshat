import uuid

from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import IntegrityError
from django.db.models import Q, ManyToManyField
from django.urls import reverse

from ..accounts.models import Seshat_Expert
from ..utils import get_color, get_date, ATTRS_HTML
from ..constants import ZOTERO

from .constants import (
    POLITY_TAG_CHOICES,
    WORLD_REGION_CHOICES,
    TAGS,
)


class SeshatPrivateComment(models.Model):
    """
    Model representing a private comment.
    """

    text = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        # Get private comment parts
        private_comment_parts = (
            self.inner_private_comments_related.all().order_by("created_date")
        )

        if private_comment_parts:
            private_comment_parts_html = []
            for private_comment_part in private_comment_parts:
                color = get_color(
                    private_comment_part.private_comment_owner.id
                )
                private_comment_parts_html.append(
                    f'<span class="badge text-dark fs-6 border border-dark" style="background:{color};">{private_comment_part.private_comment_owner}</span> {private_comment_part.private_comment_part_text}<br />'  # noqa: E501 pylint: disable=C0301
                )

            if not private_comment_parts_html:
                return " Nothing "

            return " ".join(private_comment_parts_html)

        if self.text and not private_comment_parts:
            return "No Private Comments."

        return "EMPTY_PRIVATE_COMMENT"

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("seshatprivatecomments")


class SeshatPrivateCommentPart(models.Model):
    """
    Model representing a part of a private comment.
    """

    private_comment = models.ForeignKey(
        SeshatPrivateComment,
        on_delete=models.SET_NULL,
        related_name="inner_private_comments_related",
        related_query_name="inner_private_comments_related",
        null=True,
        blank=True,
    )
    private_comment_part_text = models.TextField(
        blank=True,
        null=True,
    )
    private_comment_owner = models.ForeignKey(
        Seshat_Expert,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )
    private_comment_reader = models.ManyToManyField(
        Seshat_Expert,
        related_name="%(app_label)s_%(class)s_readers_related",
        related_query_name="%(app_label)s_%(class)ss_readers",
        blank=True,
    )
    created_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    last_modified_date = models.DateTimeField(
        auto_now=True, blank=True, null=True
    )

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse(
            "seshatprivatecomment-update", args=[self.private_comment.id]
        )

    class Meta:
        """
        :noindex:
        """

        ordering = ["created_date", "last_modified_date"]

    def __str__(self) -> str:
        if self.private_comment_part_text:
            return self.private_comment_part_text

        return "NO_Private_COMMENTS_TO_SHOW"


class Macro_region(models.Model):
    """
    Model representing a macro region.
    """

    name = models.CharField(max_length=100)

    class Meta:
        """
        :noindex:
        """

        ordering = [
            "name",
        ]

    def __str__(self) -> str:
        return self.name


class Seshat_region(models.Model):
    """
    Model representing a Seshat region.
    """

    name = models.CharField(max_length=100)
    mac_region = models.ForeignKey(
        Macro_region,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mac_region",
    )
    subregions_list = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        ordering = ["mac_region__name", "name"]

    def __str__(self) -> str:
        if self.mac_region:
            return f"{self.name} ({self.mac_region.name})"

        return self.name


class Nga(models.Model):
    """
    Model representing a NGA.
    """

    name = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=16, decimal_places=12, blank=True, null=True
    )
    latitude = models.DecimalField(
        max_digits=16, decimal_places=12, blank=True, null=True
    )
    capital_city = models.CharField(max_length=100, blank=True, null=True)
    nga_code = models.CharField(max_length=20, blank=True, null=True)
    fao_country = models.CharField(max_length=100, blank=True, null=True)
    world_region = models.CharField(
        max_length=100,
        choices=WORLD_REGION_CHOICES,
        default="Europe",
        null=True,
        blank=True,
    )

    class Meta:
        """
        :noindex:
        """

        ordering = ["name"]

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("ngas")

    def __str__(self) -> str:
        return self.name


class Polity(models.Model):
    """
    Model representing a polity.
    """

    name = models.CharField(max_length=100)
    start_year = models.IntegerField(blank=True, null=True)
    end_year = models.IntegerField(blank=True, null=True)
    long_name = models.CharField(max_length=200, blank=True, null=True)
    new_name = models.CharField(max_length=100, blank=True, null=True)
    home_nga = models.ForeignKey(
        Nga,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="home_nga",
    )
    home_seshat_region = models.ForeignKey(
        Seshat_region,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="home_seshat_region",
    )
    polity_tag = models.CharField(
        max_length=100,
        choices=POLITY_TAG_CHOICES,
        default="OTHER_TAG",
        null=True,
        blank=True,
    )
    general_description = models.TextField(
        blank=True,
        null=True,
    )
    shapefile_name = models.CharField(max_length=300, blank=True, null=True)
    private_comment = models.TextField(
        blank=True,
        null=True,
    )
    private_comment_n = models.ForeignKey(
        SeshatPrivateComment,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        verbose_name = "polity"
        verbose_name_plural = "polities"
        unique_together = ("name",)
        ordering = ["long_name"]

    def clean(self) -> None:
        """
        Verifies a number of conditions on the start and end years of the polity.

        Raises:
            ValidationError: If the start year is greater than the end year.
            ValidationError: If the end year is greater than the current year.
            ValidationError: If the start year is greater than the current year.

        Returns:
            None
        """
        current_year = get_date("%Y")

        if (
            self.start_year is not None
            and self.end_year is not None
            and self.start_year > self.end_year
        ):
            raise ValidationError(
                "Start year cannot be greater than end year."
            )

        if self.end_year is not None and self.end_year > current_year:
            raise ValidationError(
                "End year cannot be greater than the current year"
            )

        if self.start_year is not None and self.start_year > current_year:
            raise ValidationError(
                "Start year cannot be greater than the current year"
            )

        return None

    def __str__(self) -> str:
        if self.long_name and self.new_name:
            return f"{self.long_name} ({self.new_name})"

        return self.name


class Capital(models.Model):
    """
    Model representing a capital.
    """

    name = models.CharField(max_length=100)
    alternative_names = models.CharField(max_length=300, blank=True, null=True)
    current_country = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=11, decimal_places=8, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=11, decimal_places=8, blank=True, null=True
    )
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(
        blank=True,
        null=True,
    )
    url_on_the_map = models.URLField(max_length=200, blank=True, null=True)
    is_verified = models.BooleanField(default=False, blank=True, null=True)
    note = models.TextField(
        blank=True,
        null=True,
    )

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("capitals")

    def __str__(self) -> str:
        if self.name and self.alternative_names:
            f"{self.name} [{self.alternative_names}]"

        return self.name

    class Meta:
        """
        :noindex:
        """

        ordering = ["is_verified"]


class Ngapolityrel(models.Model):
    """
    Model representing a relationship between a NGA and a polity.
    """

    name = models.CharField(max_length=200, blank=True, null=True)
    polity_party = models.ForeignKey(
        Polity,
        on_delete=models.SET_NULL,
        null=True,
        related_name="polity_sides",
    )
    nga_party = models.ForeignKey(
        Nga, on_delete=models.SET_NULL, null=True, related_name="nga_sides"
    )
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(
        blank=True,
        null=True,
    )
    is_home_nga = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        if self.name:
            return self.name

        if self.polity_party and self.nga_party:
            return f"{self.polity_party.name}'s settlement in {self.nga_party.name}"

        return str(self.id)


class Country(models.Model):
    """
    Model representing a country.
    """

    name = models.CharField(max_length=200)
    polity = models.ForeignKey(
        Polity, on_delete=models.SET_NULL, null=True, related_name="countries"
    )

    class Meta:
        """
        :noindex:
        """

        verbose_name = "country"
        verbose_name_plural = "countries"
        unique_together = ("name",)

    def __str__(self) -> str:
        return self.name


class Section(models.Model):
    """
    Model representing a section.
    """

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

    class Meta:
        """
        :noindex:
        """

        unique_together = ("name",)


class Subsection(models.Model):
    """
    Model representing a subsection.
    """

    name = models.CharField(max_length=200)
    section = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        related_name="subsections",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        """
        :noindex:
        """

        unique_together = ("name", "section")


class Variablehierarchy(models.Model):
    """
    Model representing a variable hierarchy.
    """

    name = models.CharField(max_length=200)
    section = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    subsection = models.ForeignKey(
        Subsection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_verified = models.BooleanField(default=False)
    explanation = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        """
        :noindex:
        """

        unique_together = ("name", "section", "subsection")


class Reference(models.Model):
    """
    Model Representing a reference.
    """

    title = models.CharField(
        max_length=500,
    )
    year = models.IntegerField(
        blank=True,
        null=True,
    )
    creator = models.CharField(
        max_length=500,
    )
    zotero_link = models.CharField(max_length=500, blank=True, null=True)
    long_name = models.CharField(max_length=500, blank=True, null=True)
    url_link = models.TextField(
        max_length=500, validators=[URLValidator()], blank=True, null=True
    )
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        original_title = self.title

        if len(original_title) > 60:
            last_word = original_title[60:].split(" ")[0]
            shorter_title = f"{original_title[0:60]} {last_word} ..."
        else:
            shorter_title = original_title

        if self.year:
            return f"({self.creator}_{self.year}): {shorter_title}"

        return f"({self.creator}_XXXX): {shorter_title}"

    @property
    def reference_short_title(self) -> str:
        """
        Returns a short title for the reference. If the title is longer than
        60 characters, it is truncated. If the title is not provided, a default
        title is returned.

        Returns:
            str: A short title for the reference.
        """
        shorter_name = ""

        # Set shorter_name to the first 60 characters of the long_name
        if self.long_name and len(self.long_name) > 60:
            last_word = self.long_name[60:].split(" ")[0]
            shorter_name = f"{self.long_name[0:60]} {last_word} ..."
        elif self.long_name:
            shorter_name = self.long_name
        else:
            shorter_name = "BlaBla"

        # If the zotero link is not provided, return a default title
        if self.zotero_link and "NOZOTERO_LINK" in self.zotero_link:
            return f"(NOZOTERO_REF: {shorter_name})"

        # If there is a title, return the title
        if self.title:
            return self.title

        return "NO_TITLES_PROVIDED"

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("references")

    class Meta:
        """
        :noindex:
        """

        unique_together = ("zotero_link",)
        ordering = ["-created_date", "title"]


class Citation(models.Model):
    """
    Model representing a specific citation.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique Id for this particular citation",
    )
    ref = models.ForeignKey(
        Reference,
        on_delete=models.SET_NULL,
        null=True,
        related_name="citation",
    )
    page_from = models.IntegerField(null=True, blank=True)
    page_to = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def zoteroer(self) -> str:
        """
        Returns the Zotero link for the citation.

        Returns:
            str: The Zotero link for the citation.
        """
        if (
            self.ref.zotero_link
            and "NOZOTERO_LINK" not in self.ref.zotero_link
        ):
            return f"{ZOTERO.BASEURL}{self.ref.zotero_link}"

        return reverse("citation-update", args=[self.id])

    def __str__(self) -> str:
        if self.ref and self.ref.title:
            original_title = self.ref.title
        else:
            original_title = "REFERENCE_WITH_NO_TITLE"

        if original_title and len(original_title) > 50:
            last_word = original_title[50:].split(" ")[0]
            short_title = f"{original_title[0:50]} {last_word}..."
        elif original_title:
            short_title = original_title
        else:
            short_title = "BlaBlaBla"

        if self.ref and self.ref.long_name:
            self.ref.long_name = self.ref.long_name
        else:
            self.ref.long_name = "REFERENCE_WITH_NO_LONG_NAME"
        if self.ref.long_name and len(self.ref.long_name) > 50:
            last_word = self.ref.long_name[50:].split(" ")[0]
            shorter_name = f"{self.ref.long_name[0:50]} {last_word}..."
        elif self.ref.long_name:
            shorter_name = self.ref.long_name
        else:
            shorter_name = "BlaBla"

        if (
            self.ref
            and self.ref.zotero_link
            and "NOZOTERO_LINK" in self.ref.zotero_link
        ):
            return f"(NOZOTERO: {shorter_name})"

        if self.ref and self.ref.creator:
            if self.page_from is None and self.page_to is None:
                return f"({self.ref.creator} {self.ref.year}): {short_title}"
            elif self.page_from == self.page_to or (
                (not self.page_to) and self.page_from
            ):
                return f"({self.ref.creator} {self.ref.year}, p. {self.page_from}): {short_title}"  # noqa: E501 pylint: disable=C0301
            elif self.page_from == self.page_to or (
                (not self.page_from) and self.page_to
            ):
                return f"({self.ref.creator} {self.ref.year}, p. {self.page_to}): {short_title}"  # noqa: E501 pylint: disable=C0301
            elif self.page_from and self.page_to:
                return f"({self.ref.creator} {self.ref.year}, pp. {self.page_from}-{self.page_to}): {short_title}"  # noqa: E501 pylint: disable=C0301
            else:
                return "({self.ref.creator} {self.ref.year}): {shorter_title}"
        else:
            return "BADBADREFERENCE"

    def full_citation_display(self) -> str:
        """
        Returns a string of the full citation. If the citation has a title, it
        is included in the string. If the citation has a creator, it is
        included in the string. If the citation has a year, it is included in
        the string. If the citation has a page_from, it is included in the
        string. If the citation has a page_to, it is included in the string.

        Returns:
            str: A string of the full citation.
        """
        if self.ref and self.ref.title:
            original_title = self.ref.title
        else:
            original_title = "REFERENCE_WITH_NO_TITLE"

        if original_title:
            shorter_title = original_title
        else:
            shorter_title = "BlaBlaBla"

        if self.ref and self.ref.long_name:
            self.ref.long_name = self.ref.long_name
        else:
            self.ref.long_name = "REFERENCE_WITH_NO_LONG_NAME"

        if self.ref.long_name:
            shorter_name = self.ref.long_name
        else:
            shorter_name = "BlaBla"

        if (
            self.ref
            and self.ref.zotero_link
            and "NOZOTERO_LINK" in self.ref.zotero_link
        ):
            return f"(NOZOTERO: {shorter_name})"

        if self.ref and self.ref.creator:
            if self.page_from is None and self.page_to is None:
                return f"<b {ATTRS_HTML.text_bold}>({self.ref.creator} {self.ref.year})</b>: {shorter_title}"  # noqa: E501 pylint: disable=C0301

            if self.page_from == self.page_to or (
                (not self.page_to) and self.page_from
            ):
                return f"<b {ATTRS_HTML.text_bold}>({self.ref.creator} {self.ref.year}, p. {self.page_from})</b>: {shorter_title}"  # noqa: E501 pylint: disable=C0301

            if self.page_from == self.page_to or (
                (not self.page_from) and self.page_to
            ):
                return f"<b {ATTRS_HTML.text_bold}>({self.ref.creator} {self.ref.year}, p. {self.page_to})</b>: {shorter_title}"  # noqa: E501 pylint: disable=C0301

            if self.page_from and self.page_to:
                return f"<b {ATTRS_HTML.text_bold}>({self.ref.creator} {self.ref.year}, pp. {self.page_from}-{self.page_to})</b>: {shorter_title}"  # noqa: E501 pylint: disable=C0301

            return f"<b {ATTRS_HTML.text_bold}>({self.ref.creator} {self.ref.year})</b>: {shorter_title}"  # noqa: E501 pylint: disable=C0301

        return "BADBADREFERENCE"

    class Meta:
        """
        :noindex:
        """

        ordering = ["-modified_date"]
        constraints = [
            models.UniqueConstraint(
                name="No_PAGE_TO_AND_FROM",
                fields=("ref",),
                condition=(
                    Q(page_to__isnull=True) & Q(page_from__isnull=True)
                ),
            ),
            models.UniqueConstraint(
                name="No_PAGE_TO",
                fields=("ref", "page_from"),
                condition=Q(page_to__isnull=True),
            ),
            models.UniqueConstraint(
                name="No_PAGE_FROM",
                fields=("ref", "page_to"),
                condition=Q(page_from__isnull=True),
            ),
        ]

    @property
    def citation_short_title(self) -> str:
        """
        Returns a short title for the citation. If the title is longer than
        40 characters, it is truncated. If the title is not provided, a default
        title is returned.

        Returns:
            str: A short title for the citation.
        """
        if self.ref.long_name and len(self.ref.long_name) > 40:
            shorter_name = (
                self.ref.long_name[0:40]
                + self.ref.long_name[40:].split(" ")[0]
                + "..."
            )
        elif self.ref.long_name:
            shorter_name = self.ref.long_name
        else:
            # TODO: Does this ever happen? If so, should we handle it differently?
            # (shorter_name = "BlaBla" doesn't seem helpful)
            shorter_name = "BlaBla"

        if "NOZOTERO_LINK" in self.ref.zotero_link:
            return f"(NOZOTERO: {shorter_name})"

        if self.page_from is None and self.page_to is None:
            return f"[{self.ref.creator} {self.ref.year}]"

        if self.page_from == self.page_to or (
            (not self.page_to) and self.page_from
        ):
            return f"[{self.ref.creator} {self.ref.year}, p. {self.page_from}]"

        if self.page_from == self.page_to or (
            (not self.page_from) and self.page_to
        ):
            return f"[{self.ref.creator} {self.ref.year}, p. {self.page_to}]"

        if self.page_from and self.page_to:
            return f"[{self.ref.creator} {self.ref.year}, pp. {self.page_from}-{self.page_to}]"  # noqa: E501 pylint: disable=C0301

        return f"[{self.ref.creator} {self.ref.year}]"

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("citations")

    def save(self, *args, **kwargs):
        """
        Saves the citation to the database.

        Args:
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.

        Raises:
            IntegrityError: If the citation cannot be saved to the database.

        Returns:
            None
        """
        try:
            super(Citation, self).save(*args, **kwargs)
        except IntegrityError as e:
            print(e)  # TODO: We probably want to handle this differently


class SeshatComment(models.Model):
    """
    Model representing a comment.
    """

    text = models.TextField(
        blank=True,
        null=True,
    )

    def zoteroer(self):
        """
        Returns the Zotero link for the comment. If the comment has a Zotero
        link, it is returned. Otherwise, a default link (#) is returned.

        Returns:
            str: The Zotero link for the comment.
        """
        if (
            self.ref.zotero_link
            and "NOZOTERO_LINK" not in self.ref.zotero_link
        ):
            return f"{ZOTERO.BASEURL}{self.ref.zotero_link}"

        return "#"

    def __str__(self) -> str:
        inner_comments = self.inner_comments_related.all()

        if not inner_comments and self.text:
            return "No descriptions."

        if not inner_comments:
            return "EMPTY_COMMENT"

        comment_parts = []
        for comment in inner_comments.order_by("comment_order"):
            if comment.citation_index:
                separation_point = comment.citation_index
                before, after = (
                    comment.comment_part_text[0:separation_point],
                    comment.comment_part_text[separation_point:],
                )
                text = f"{before}{comment.display_citations_plus} {after}"
            else:
                text = comment.comment_part_text if comment.comment_part_text else ""
                text = text.strip("<br>")  # drop any leading <br> tags

                if comment.display_citations_plus:
                    text = f"{text}{comment.display_citations_plus}"

            comment_parts.append(text)

        # Drop empty strings
        comment_parts = [x for x in comment_parts if x]

        if not comment_parts:
            return " Nothing "

        return " ".join(comment_parts)

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("seshatcomments")


class SeshatCommentPart(models.Model):
    """
    Model representing a part of a comment.
    """

    comment = models.ForeignKey(
        SeshatComment,
        on_delete=models.SET_NULL,
        related_name="inner_comments_related",
        related_query_name="inner_comments_related",
        null=True,
        blank=True,
    )
    comment_part_text = models.TextField(
        blank=True,
        null=True,
    )
    comment_citations_plus = models.ManyToManyField(
        Citation,
        through="ScpThroughCtn",
        related_name="%(app_label)s_%(class)s_related_through",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    comment_curator = models.ForeignKey(
        Seshat_Expert,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )
    comment_order = models.IntegerField(
        blank=True,
        null=True,
    )
    comment_citations = ManyToManyField(
        Citation,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    citation_index = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    @property
    def citations_count(self):
        """
        Returns the number of citations for a comment.

        Returns:
            int: The number of citations for a comment.
        """
        return self.comment_citations.count()

    def get_citations_plus_for_comments(self):
        scp_tr = ScpThroughCtn.objects.filter(seshatcommentpart=self.id)

        return ", ".join(
            [
                f' <a href="{x.citation.zoteroer()}">{x.citation.citation_short_title}</a>'  # noqa: E501 pylint: disable=C0301
                for x in scp_tr
            ]
        )

    @property
    def display_citations(self):
        """
        Display the citations of the model instance.

        :noindex:

        Note:
            The method is a property.

        Returns:
            str: The citations of the model instance, separated by comma.
        """
        if self.comment_citations.all():
            return ", ".join(
                [
                    f' <a href="{citation.zoteroer()}">{citation.citation_short_title}</a>'
                    for citation in self.comment_citations.all()
                ]
            )

        return ""

    @property
    def display_citations_plus(self):
        """
        Returns a string of all the citations for a comment.

        :noindex:

        Note:
            The method is a property.

        Returns:
            str: A string of all the citations for a comment.
        """
        x = self.get_citations_plus_for_comments()
        y = self.display_citations

        if x and y:
            return x + y

        if x:
            return x

        return y

    @property
    def citations_count_plus(self):
        """
        Returns the number of citations for a comment.

        Returns:
            int: The number of citations for a comment.
        """
        return ScpThroughCtn.objects.filter(seshatcommentpart=self.id).count()

    def get_absolute_url(self) -> str:
        """
        Returns the url to access a particular instance of the model.

        :noindex:

        Returns:
            str: A string of the url to access a particular instance of the model.
        """
        return reverse("seshatcomment-update", args=[str(self.comment.id)])

    class Meta:
        """
        :noindex:
        """

        ordering = ["comment_order", "modified_date"]

    def __str__(self) -> str:
        if self.comment_part_text and self.display_citations_plus:
            return f"{self.comment_part_text} {self.display_citations_plus}"

        if self.comment_part_text and self.display_citations:
            return f"{self.comment_part_text} {self.display_citations}"

        if self.comment_part_text:
            return self.comment_part_text

        return "NO_SUB_COMMENTS_TO_SHOW"


class ScpThroughCtn(models.Model):
    """
    Model representing a through model for the many-to-many relationship between
    a comment part and a citation.
    """

    seshatcommentpart = models.ForeignKey(
        SeshatCommentPart,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )
    citation = models.ForeignKey(
        Citation,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )
    parent_paragraphs = models.TextField(
        blank=True,
        null=True,
    )


class SeshatCommon(models.Model):
    """
    An abstract model representing a common model for most of the models in the Seshat app.
    """

    polity = models.ForeignKey(
        Polity,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=200,
    )
    year_from = models.IntegerField(blank=True, null=True)
    year_to = models.IntegerField(
        blank=True,
        null=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    note = models.TextField(
        blank=True,
        null=True,
    )
    citations = ManyToManyField(
        Citation,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    finalized = models.BooleanField(default=False)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True
    )
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    tag = models.CharField(max_length=5, choices=TAGS, default="TRS")
    is_disputed = models.BooleanField(default=False, blank=True, null=True)
    is_uncertain = models.BooleanField(default=False, blank=True, null=True)
    expert_reviewed = models.BooleanField(null=True, blank=True, default=True)
    drb_reviewed = models.BooleanField(null=True, blank=True, default=False)
    curator = models.ManyToManyField(
        Seshat_Expert,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    comment = models.ForeignKey(
        SeshatComment,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )
    private_comment = models.ForeignKey(
        SeshatPrivateComment,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)s",
        null=True,
        blank=True,
    )

    class Meta:
        """
        :noindex:
        """

        abstract = True
        ordering = ["polity"]

    class Code:
        """
        :noindex:
        """

        section = None
        subsection = None
        variable = ""
        notes = ""
        description = ""
        description_source = ""
        inner_variables = {}


class Religion(models.Model):
    """
    Model representing a religion.
    """

    name = models.CharField(max_length=100, default="Religion")
    religion_name = models.CharField(max_length=100, null=True, blank=True)
    religion_family = models.CharField(max_length=100, blank=True, null=True)
    religion_genus = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        """
        :noindex:
        """

        ordering = ["name"]

    def __str__(self) -> str:
        if self.religion_name:
            return self.religion_name

        return self.name


# Shapefile models


class VideoShapefile(models.Model):
    """
    Model representing a video shapefile.
    """

    id = models.AutoField(primary_key=True)
    geom = models.MultiPolygonField()
    simplified_geom = models.MultiPolygonField(null=True)
    name = models.CharField(max_length=100)
    polity = models.CharField(max_length=100)
    wikipedia_name = models.CharField(max_length=100, null=True)
    seshat_id = models.CharField(max_length=100)
    area = models.FloatField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    polity_start_year = models.IntegerField()
    polity_end_year = models.IntegerField()
    colour = models.CharField(max_length=7)

    def __str__(self) -> str:
        return f"Name: {self.name}"


class GADMShapefile(models.Model):
    """ """

    geom = models.MultiPolygonField()
    UID = models.BigIntegerField()
    GID_0 = models.CharField(max_length=100, null=True)
    NAME_0 = models.CharField(max_length=100, null=True)
    VARNAME_0 = models.CharField(max_length=100, null=True)
    GID_1 = models.CharField(max_length=100, null=True)
    NAME_1 = models.CharField(max_length=100, null=True)
    VARNAME_1 = models.CharField(max_length=100, null=True)
    NL_NAME_1 = models.CharField(max_length=100, null=True)
    ISO_1 = models.CharField(max_length=100, null=True)
    HASC_1 = models.CharField(max_length=100, null=True)
    CC_1 = models.CharField(max_length=100, null=True)
    TYPE_1 = models.CharField(max_length=100, null=True)
    ENGTYPE_1 = models.CharField(max_length=100, null=True)
    VALIDFR_1 = models.CharField(max_length=100, null=True)
    GID_2 = models.CharField(max_length=100, null=True)
    NAME_2 = models.CharField(max_length=100, null=True)
    VARNAME_2 = models.CharField(max_length=100, null=True)
    NL_NAME_2 = models.CharField(max_length=100, null=True)
    HASC_2 = models.CharField(max_length=100, null=True)
    CC_2 = models.CharField(max_length=100, null=True)
    TYPE_2 = models.CharField(max_length=100, null=True)
    ENGTYPE_2 = models.CharField(max_length=100, null=True)
    VALIDFR_2 = models.CharField(max_length=100, null=True)
    GID_3 = models.CharField(max_length=100, null=True)
    NAME_3 = models.CharField(max_length=100, null=True)
    VARNAME_3 = models.CharField(max_length=100, null=True)
    NL_NAME_3 = models.CharField(max_length=100, null=True)
    HASC_3 = models.CharField(max_length=100, null=True)
    CC_3 = models.CharField(max_length=100, null=True)
    TYPE_3 = models.CharField(max_length=100, null=True)
    ENGTYPE_3 = models.CharField(max_length=100, null=True)
    VALIDFR_3 = models.CharField(max_length=100, null=True)
    GID_4 = models.CharField(max_length=100, null=True)
    NAME_4 = models.CharField(max_length=100, null=True)
    VARNAME_4 = models.CharField(max_length=100, null=True)
    CC_4 = models.CharField(max_length=100, null=True)
    TYPE_4 = models.CharField(max_length=100, null=True)
    ENGTYPE_4 = models.CharField(max_length=100, null=True)
    VALIDFR_4 = models.CharField(max_length=100, null=True)
    GID_5 = models.CharField(max_length=100, null=True)
    NAME_5 = models.CharField(max_length=100, null=True)
    CC_5 = models.CharField(max_length=100, null=True)
    TYPE_5 = models.CharField(max_length=100, null=True)
    ENGTYPE_5 = models.CharField(max_length=100, null=True)
    GOVERNEDBY = models.CharField(max_length=100, null=True)
    SOVEREIGN = models.CharField(max_length=100, null=True)
    DISPUTEDBY = models.CharField(max_length=100, null=True)
    REGION = models.CharField(max_length=100, null=True)
    VARREGION = models.CharField(max_length=100, null=True)
    COUNTRY = models.CharField(max_length=100, null=True)
    CONTINENT = models.CharField(max_length=100, null=True)
    SUBCONT = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"Name: {self.name}"


class GADMCountries(models.Model):
    """
    Model representing a country (GADM).
    """

    geom = models.MultiPolygonField()
    COUNTRY = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"Name: {self.name}"


class GADMProvinces(models.Model):
    """
    Model representing a province (GADM).
    """

    geom = models.MultiPolygonField()
    COUNTRY = models.CharField(max_length=100, null=True)
    NAME_1 = models.CharField(max_length=100, null=True)
    ENGTYPE_1 = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"Name: {self.name}"
