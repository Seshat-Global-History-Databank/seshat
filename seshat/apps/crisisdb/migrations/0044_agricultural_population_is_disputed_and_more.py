# Generated by Django 4.0.3 on 2023-01-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisisdb', '0043_alter_human_sacrifice_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agricultural_population',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='arable_land',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='arable_land_per_farmer',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='crop_failure_event',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='disease_outbreak',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='drought_event',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='external_conflict_side',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='famine_event',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='gdp_per_capita',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='gross_grain_shared_per_agricultural_population',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='human_sacrifice',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='internal_conflict',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='locust_event',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='military_expense',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='net_grain_shared_per_agricultural_population',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='silver_inflow',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='silver_stock',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='socioeconomic_turmoil_event',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='surplus',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='total_population',
            name='is_disputed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
