# Generated by Django 4.0.3 on 2023-05-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crisisdb", "0057_alter_power_transition_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="power_transition",
            name="predecessor",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="power_transition",
            name="successor",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
