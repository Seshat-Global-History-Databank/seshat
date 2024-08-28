# Generated by Django 4.0.3 on 2023-01-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crisisdb", "0045_alter_human_sacrifice_human_sacrifice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agricultural_population",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="arable_land",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="arable_land_per_farmer",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="crop_failure_event",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="disease_outbreak",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="drought_event",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="external_conflict",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="external_conflict_side",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="famine_event",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="gdp_per_capita",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="gross_grain_shared_per_agricultural_population",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="human_sacrifice",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="internal_conflict",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="locust_event",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="military_expense",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="net_grain_shared_per_agricultural_population",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="silver_inflow",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="silver_stock",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="socioeconomic_turmoil_event",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="surplus",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="total_population",
            name="tag",
            field=models.CharField(
                choices=[
                    ("TRS", "Evidenced"),
                    ("SSP", "Suspected"),
                    ("IFR", "Inferred"),
                ],
                default="TRS",
                max_length=5,
            ),
        ),
    ]
