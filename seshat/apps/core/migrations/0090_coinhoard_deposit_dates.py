# Generated manually for coin hoard deposit chronology fields

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0089_remove_coinhoard_core_coinho_data_so_b72e26_idx_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="coinhoard",
            name="deposit_year_from",
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name="coinhoard",
            name="deposit_year_to",
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name="coinhoard",
            name="deposit_display",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="coinhoardpolitymapping",
            name="temporal_match_basis",
            field=models.CharField(blank=True, default="", max_length=32),
        ),
        migrations.AddIndex(
            model_name="coinhoard",
            index=models.Index(
                fields=["data_source", "deposit_year_from", "deposit_year_to"],
                name="core_coinho_data_so_c2c150_idx",
            ),
        ),
    ]
