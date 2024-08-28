# Generated by Django 4.0.3 on 2022-08-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0018_remove_citation_no_page_to_or_from_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="citation",
            name="No_PAGE_TO_OR_FROM",
        ),
        migrations.AddConstraint(
            model_name="citation",
            constraint=models.UniqueConstraint(
                condition=models.Q(
                    ("page_to__isnull", True), ("page_from__isnull", True)
                ),
                fields=("ref",),
                name="No_PAGE_TO_AND_FROM",
            ),
        ),
        migrations.AddConstraint(
            model_name="citation",
            constraint=models.UniqueConstraint(
                condition=models.Q(("page_to__isnull", True)),
                fields=("ref", "page_from"),
                name="No_PAGE_TO",
            ),
        ),
        migrations.AddConstraint(
            model_name="citation",
            constraint=models.UniqueConstraint(
                condition=models.Q(("page_from__isnull", True)),
                fields=("ref", "page_to"),
                name="No_PAGE_FROM",
            ),
        ),
    ]
