from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("general", "0020_alter_polity_alternate_religion_comment_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="polity_suprapolity_relations",
            name="supra_polity_relations",
            field=models.CharField(
                choices=[
                    ("vassalage", "subject to"),
                    ("alliance", "alliance with"),
                    ("nominal allegiance", "nominally subject to"),
                    ("personal union", "personal union with"),
                    ("unknown", "unknown"),
                    ("uncoded", "uncoded"),
                    ("none", "none"),
                ],
                max_length=500,
            ),
        ),
    ]
