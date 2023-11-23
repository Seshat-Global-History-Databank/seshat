# Generated by Django 4.0.3 on 2022-09-28 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_country_options_alter_polity_options_and_more'),
        ('crisisdb', '0019_external_conflict_side_casualty_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='external_conflict',
            options={'verbose_name': 'External_conflict', 'verbose_name_plural': 'External_conflicts'},
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='citations',
            field=models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation'),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='conflict_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='finalized',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='polity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity'),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='tag',
            field=models.CharField(choices=[('TRS', 'Evidenced'), ('DSP', 'Disputed'), ('SSP', 'Suspected'), ('IFR', 'Inferred'), ('UNK', 'Unknown')], default='TRS', max_length=5),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='year_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='external_conflict',
            name='year_to',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='external_conflict',
            name='name',
            field=models.CharField(default='External_conflict', max_length=100),
        ),
        migrations.AlterField(
            model_name='external_conflict_side',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='gdp_per_capita',
            name='gdp_per_capita',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='internal_conflict',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
        migrations.AlterField(
            model_name='military_expense',
            name='expenditure',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True),
        ),
    ]