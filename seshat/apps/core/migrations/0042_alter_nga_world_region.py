# Generated by Django 4.0.3 on 2022-12-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_alter_seshatcommentpart_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nga',
            name='world_region',
            field=models.CharField(choices=[('Europe', 'Europe'), ('Southwest Asia', 'Southwest Asia'), ('Africa', 'Africa'), ('Central Eurasia', 'Central Eurasia'), ('South Asia', 'South Asia'), ('Southeast Asia', 'Southeast Asia'), ('East Asia', 'East Asia'), ('Oceania-Australia', 'Oceania-Australia'), ('North America', 'North America'), ('South America', 'South America')], default='Europe', max_length=100),
        ),
    ]
