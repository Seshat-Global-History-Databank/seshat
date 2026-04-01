# Generated manually for long CHRE permalink text / URLs

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0086_coinhoard_external_source_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coinhoard",
            name="external_source_text",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="coinhoard",
            name="external_url",
            field=models.URLField(blank=True, default="", max_length=500),
        ),
    ]
