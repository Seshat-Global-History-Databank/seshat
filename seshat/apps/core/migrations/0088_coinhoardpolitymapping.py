# Generated manually for CoinHoard <-> Polity mappings

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0087_coinhoard_long_text_and_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="CoinHoardPolityMapping",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("overlap_year_from", models.IntegerField(blank=True, null=True)),
                ("overlap_year_to", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "cliopatria_shape",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="coinhoard_mappings",
                        to="core.cliopatria",
                    ),
                ),
                (
                    "coin_hoard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="polity_mappings",
                        to="core.coinhoard",
                    ),
                ),
                (
                    "polity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="coinhoard_mappings",
                        to="core.polity",
                    ),
                ),
            ],
            options={
                "ordering": ["coin_hoard__external_dataset_id", "polity__long_name", "polity__name"],
            },
        ),
        migrations.AddConstraint(
            model_name="coinhoardpolitymapping",
            constraint=models.UniqueConstraint(
                fields=("coin_hoard", "polity", "cliopatria_shape"),
                name="uniq_coinhoard_polity_shape_mapping",
            ),
        ),
        migrations.AddIndex(
            model_name="coinhoardpolitymapping",
            index=models.Index(fields=["coin_hoard", "polity"], name="core_coinho_coin_ho_58056c_idx"),
        ),
        migrations.AddIndex(
            model_name="coinhoardpolitymapping",
            index=models.Index(
                fields=["overlap_year_from", "overlap_year_to"],
                name="core_coinho_overlap_d51f84_idx",
            ),
        ),
    ]
