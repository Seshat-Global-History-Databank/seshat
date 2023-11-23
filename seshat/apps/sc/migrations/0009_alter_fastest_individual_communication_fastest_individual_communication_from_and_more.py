# Generated by Django 4.0.3 on 2023-11-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc', '0008_largest_communication_distance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fastest_individual_communication',
            name='fastest_individual_communication_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fastest_individual_communication',
            name='fastest_individual_communication_to',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='largest_communication_distance',
            name='largest_communication_distance_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='largest_communication_distance',
            name='largest_communication_distance_to',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]