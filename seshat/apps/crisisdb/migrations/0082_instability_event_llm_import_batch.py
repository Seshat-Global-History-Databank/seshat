# Generated for explicit instability import batches.

import datetime

from django.db import migrations, models
from django.utils import timezone


BATCH_1_END = datetime.date(2025, 3, 29)
BATCH_2_END = datetime.date(2025, 4, 11)
BATCH_3_END = datetime.date(2026, 3, 1)
BATCH_1_END_DATETIME = timezone.make_aware(
    datetime.datetime.combine(BATCH_1_END, datetime.time())
)
BATCH_2_END_DATETIME = timezone.make_aware(
    datetime.datetime.combine(BATCH_2_END, datetime.time())
)
BATCH_3_END_DATETIME = timezone.make_aware(
    datetime.datetime.combine(BATCH_3_END, datetime.time())
)


def backfill_llm_import_batches(apps, schema_editor):
    InstabilityEvent = apps.get_model("crisisdb", "Instability_event")
    db_alias = schema_editor.connection.alias
    llm_events = InstabilityEvent.objects.using(db_alias).filter(source="llm")

    llm_events.filter(created_date__lt=BATCH_1_END_DATETIME).update(
        llm_import_batch="Batch 1"
    )
    llm_events.filter(
        created_date__gte=BATCH_1_END_DATETIME,
        created_date__lt=BATCH_2_END_DATETIME,
    ).update(llm_import_batch="Batch 2")
    llm_events.filter(
        created_date__gte=BATCH_2_END_DATETIME,
        created_date__lt=BATCH_3_END_DATETIME,
    ).update(llm_import_batch="Batch 3")
    llm_events.filter(created_date__gte=BATCH_3_END_DATETIME).update(
        llm_import_batch="Batch 4"
    )


def clear_llm_import_batches(apps, schema_editor):
    InstabilityEvent = apps.get_model("crisisdb", "Instability_event")
    db_alias = schema_editor.connection.alias
    InstabilityEvent.objects.using(db_alias).filter(source="llm").update(
        llm_import_batch=None
    )


class Migration(migrations.Migration):

    dependencies = [
        ("crisisdb", "0081_alter_instability_event_inst_intensity_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="instability_event",
            name="llm_import_batch",
            field=models.CharField(
                blank=True,
                db_index=True,
                max_length=50,
                null=True,
            ),
        ),
        migrations.RunPython(backfill_llm_import_batches, clear_llm_import_batches),
    ]
