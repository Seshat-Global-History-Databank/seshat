# Generated by Django 4.0.3 on 2023-05-29 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crisisdb", "0054_alter_power_transition_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="power_transition",
            name="culture_group",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
