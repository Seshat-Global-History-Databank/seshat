# Generated by Django 4.0.3 on 2024-03-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0057_scpthroughctn_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="polity",
            name="shapefile_name",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
