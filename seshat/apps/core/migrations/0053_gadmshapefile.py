# Generated by Django 4.0.3 on 2023-11-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_macrostateshapefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GADMShapefile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
