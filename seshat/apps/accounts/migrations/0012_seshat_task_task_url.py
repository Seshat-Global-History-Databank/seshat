# Generated by Django 4.0.3 on 2022-10-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_seshat_task"),
    ]

    operations = [
        migrations.AddField(
            model_name="seshat_task",
            name="task_url",
            field=models.TextField(blank=True, null=True),
        ),
    ]
