from django.urls import reverse
from ..utils import deprecated


class ZoteroMixIn:
    @property
    def __no_zotero_link__(self) -> str:
        return reverse("citation-update", args=[self.id])

    @property
    def has_zotero(self) -> bool:
        return self.ref.has_zotero

    @property
    def zotero_link(self) -> str:
        """
        Returns the Zotero link for the citation.

        Returns:
            str: The Zotero link for the citation.
        """
        if self.has_zotero:
            return self.ref.full_zotero_link

        return self.__no_zotero_link__

    @deprecated
    def zoteroer(self) -> str:
        """
        For backward compatibility, this method returns the Zotero link for the citation.

        Returns:
            str: The Zotero link for the citation.

        Deprecated:
            Use the `zotero_link` property instead.
        """
        return self.zotero_link
