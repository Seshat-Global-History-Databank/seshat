# Generated by Django 4.0.3 on 2022-09-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_seshat_expert"),
    ]

    operations = [
        migrations.AlterField(
            model_name="seshat_expert",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[
                    (1, "Seshat Admin"),
                    (2, "Research Assistant"),
                    (3, "Seshat Expert"),
                ],
                max_length=60,
                null=True,
            ),
        ),
    ]
