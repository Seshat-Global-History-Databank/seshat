# Generated by Django 4.0.3 on 2024-04-08 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0061_seshatprivatecomment_seshatprivatecommentpart"),
        ("wf", "0004_alter_atlatl_tag_alter_battle_axe_tag_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="atlatl",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="battle_axe",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="breastplate",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="bronze",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="camel",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="chainmail",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="complex_fortification",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="composite_bow",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="copper",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="crossbow",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="dagger",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="ditch",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="dog",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="donkey",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="earth_rampart",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="elephant",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="fortified_camp",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="gunpowder_siege_artillery",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="handheld_firearm",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="helmet",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="horse",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="iron",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="javelin",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="laminar_armor",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="leather_cloth",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="limb_protection",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="long_wall",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="merchant_ships_pressed_into_service",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="moat",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="modern_fortification",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="plate_armor",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="polearm",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="scaled_armor",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="self_bow",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="settlements_in_a_defensive_position",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="shield",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="sling",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="sling_siege_engine",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="small_vessels_canoes_etc",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="spear",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="specialized_military_vessel",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="steel",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="stone_walls_mortared",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="stone_walls_non_mortared",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="sword",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="tension_siege_engine",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="war_club",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="wood_bark_etc",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
        migrations.AddField(
            model_name="wooden_palisade",
            name="private_comment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)s",
                to="core.seshatprivatecomment",
            ),
        ),
    ]
