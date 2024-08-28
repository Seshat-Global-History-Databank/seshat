# Generated by Django 4.0.3 on 2023-08-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0048_alter_citation_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nga",
            name="world_region",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Europe", "Europe"),
                    ("Southwest Asia", "Southwest Asia"),
                    ("Africa", "Africa"),
                    ("Central Eurasia", "Central Eurasia"),
                    ("South Asia", "South Asia"),
                    ("Southeast Asia", "Southeast Asia"),
                    ("East Asia", "East Asia"),
                    ("Oceania-Australia", "Oceania-Australia"),
                    ("North America", "North America"),
                    ("South America", "South America"),
                ],
                default="Europe",
                max_length=100,
                null=True,
            ),
        ),
    ]
