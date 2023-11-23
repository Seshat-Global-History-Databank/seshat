# Generated by Django 4.0.3 on 2023-05-10 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_seshat_task_task_url'),
        ('core', '0047_polity_home_nga'),
        ('crisisdb', '0048_agricultural_population_is_uncertain_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crisis_consequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year_from', models.IntegerField(blank=True, null=True)),
                ('year_to', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('finalized', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('tag', models.CharField(choices=[('TRS', 'Evidenced'), ('SSP', 'Suspected'), ('IFR', 'Inferred')], default='TRS', max_length=5)),
                ('is_disputed', models.BooleanField(blank=True, default=False, null=True)),
                ('is_uncertain', models.BooleanField(blank=True, default=False, null=True)),
                ('expert_reviewed', models.BooleanField(blank=True, default=True, null=True)),
                ('drb_reviewed', models.BooleanField(blank=True, default=False, null=True)),
                ('crisis_case_id', models.CharField(max_length=100)),
                ('is_first_100', models.BooleanField(blank=True, default=False, null=True)),
                ('decline', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('collapse', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('epidemic', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('downward_mobility', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('extermination', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('uprising', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('revolution', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('successful_revolution', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('civil_war', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('century_plus', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('fragmentation', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('capital', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('conquest', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('assassination', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('depose', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('constitution', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('labor', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('unfree_labor', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('suffrage', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('public_goods', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('religion', models.CharField(choices=[('U', 'Unknown'), ('SU', 'Suspected Unknown'), ('P', 'Present'), ('A', 'Absent'), ('IP', 'Inferred Present'), ('IA', 'Inferred Absent')], max_length=5)),
                ('citations', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='core.citation')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.seshatcomment')),
                ('curator', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)ss', to='accounts.seshat_expert')),
                ('other_polity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related_other', related_query_name='%(app_label)s_%(class)s_other', to='core.polity')),
                ('polity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related', related_query_name='%(app_label)s_%(class)s', to='core.polity')),
            ],
            options={
                'verbose_name': 'Crisis_consequence',
                'verbose_name_plural': 'Crisis_consequences',
                'ordering': ['year_from', 'year_to'],
            },
        ),
    ]