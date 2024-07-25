# Generated by Django 4.0.3 on 2024-07-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_rename_videoshapefile_cliopatria'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliopatria',
            name='confidence',
            field=models.IntegerField(choices=[(1, 'Approximate'), (2, 'Moderate precision'), (3, 'Determined by international law')], null=True),
        ),
    ]
