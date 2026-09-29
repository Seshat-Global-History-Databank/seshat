import re

from django.db import migrations


OLD_DESCRIPTION = """unknown/ none/ alliance/ nominal allegiance/ personal union/ vassalage/

'alliance' = belongs to a long-term military-political alliance of independent polities ('long-term' refers to more or less permanent relationship between polities extending over multiple years)
'nominal allegiance' = same as 'nominal' under the variable "Degree of centralization" but now reflecting the position of the focal polity within the overarching political authority
'personal union' = the focal polity is united with another, or others, as a result of a dynastic marriage
'vassalage' = corresponding to 'loose' category in the Degree of centralization"""

NEW_DESCRIPTION = """unknown/ none/ alliance/ personal union/ subject to/ nominally subject to/

'alliance' = belongs to a long-term military-political alliance of independent polities ('long-term' refers to more or less permanent relationship between polities extending over multiple years)
'personal union' = the focal polity is united with another, or others, as a result of a dynastic marriage
'subject to' = the polity is subject to political, economic, and/or military control by another state. Includes vassalage, colonial domination, or consistent external interference. May be part of a larger structure (e.g., Holy Roman Empire or South Asian mandala system).
'nominally subject to' = the polity pays formal allegiance (e.g., acknowledges the suzerainty of) to another polity while maintaining political, military, and economic independence. Often corresponds to “nominal” under the degree of centralization of the dominant polity."""

SUBJECT_HTML = ("<li><strong>subject to:</strong> the polity is subject to political, "
                "economic, and/or military control by another state. Includes vassalage, "
                "colonial domination, or consistent external interference. May be part of "
                "a larger structure (e.g., Holy Roman Empire or South Asian mandala system).</li>")
NOMINAL_HTML = ("<li><strong>nominally subject to:</strong> the polity pays formal allegiance "
                "(e.g., acknowledges the suzerainty of) to another polity while maintaining "
                "political, military, and economic independence. Often corresponds to “nominal” "
                "under the degree of centralization of the dominant polity.</li>")

SUBJECT_ITEM = re.compile(
    r"<li>\s*<strong>\s*(?:vassal state of|vassalage to|vassalage|subject to):\s*</strong>.*?</li>",
    re.IGNORECASE | re.DOTALL,
)
NOMINAL_ITEM = re.compile(
    r"<li>\s*<strong>\s*(?:nominal allegiance to|nominal allegiance|nominally subject to):\s*</strong>.*?</li>",
    re.IGNORECASE | re.DOTALL,
)


def revised_explanation(description):
    if not description or description == OLD_DESCRIPTION:
        return NEW_DESCRIPTION

    subject = SUBJECT_ITEM.search(description)
    nominal = NOMINAL_ITEM.search(description)
    if not (subject and nominal):
        raise ValueError("Unrecognized supra-polity codebook format; review before replacing it")

    first, second = sorted((subject, nominal), key=lambda item: item.start())
    return (description[:first.start()] + SUBJECT_HTML
            + description[first.end():second.start()] + NOMINAL_HTML
            + description[second.end():])


def update_codebook(apps, schema_editor):
    Variablehierarchy = apps.get_model("core", "Variablehierarchy")
    entries = Variablehierarchy.objects.using(schema_editor.connection.alias).filter(
        name="Polity Suprapolity Relations",
        section__seshat_db_section="General",
    )
    for entry in entries:
        Variablehierarchy.objects.using(schema_editor.connection.alias).filter(
            pk=entry.pk,
        ).update(explanation=revised_explanation(entry.explanation))


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0090_coinhoard_deposit_dates"),
        ("general", "0021_update_suprapolity_relation_labels"),
    ]

    operations = [
        migrations.RunPython(update_codebook, migrations.RunPython.noop),
    ]
