# Generated by Django 4.0.3 on 2022-10-04 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_seshatcomment_seshatcommentpart"),
        ("crisisdb", "0033_remove_agricultural_population_comment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="agricultural_population",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="arable_land",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="arable_land_per_farmer",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="crop_failure_event",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="disease_outbreak",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="drought_event",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="external_conflict",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="external_conflict_side",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="famine_event",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="gdp_per_capita",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="gross_grain_shared_per_agricultural_population",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="internal_conflict",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="locust_event",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="military_expense",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="net_grain_shared_per_agricultural_population",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="silver_inflow",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="silver_stock",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="socioeconomic_turmoil_event",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="surplus",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
        migrations.AddField(
            model_name="total_population",
            name="comment",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatcomment",
            ),
        ),
    ]
