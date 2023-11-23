# Generated by Django 4.0.3 on 2022-09-30 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crisisdb', '0023_alter_agricultural_population_polity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arable_land',
            name='curator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]