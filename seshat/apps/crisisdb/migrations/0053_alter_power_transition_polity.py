# Generated by Django 4.0.3 on 2023-05-24 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0047_polity_home_nga"),
        ("crisisdb", "0052_alter_crisis_consequence_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="power_transition",
            name="polity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.polity",
            ),
        ),
    ]
