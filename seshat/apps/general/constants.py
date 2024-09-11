__all__ = [
    "APP_NAME",
    "POLITY_ALTERNATE_RELIGION_CHOICES",
    "POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES",
    "POLITY_ALTERNATE_RELIGION_GENUS_CHOICES",
    "POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES",
    "POLITY_RELIGION_CHOICES",
    "POLITY_RELIGION_FAMILY_CHOICES",
    "POLITY_RELIGION_GENUS_CHOICES",
    "POLITY_SUPRAPOLITY_RELATIONS_CHOICES",
    "POLITY_CONSECUTIVE_ENTITY_CHOICES",
    "POLITY_DEGREE_OF_CENTRALIZATION_CHOICES",
]

APP_NAME = "general"

POLITY_DEGREE_OF_CENTRALIZATION_CHOICES = (
    ("loose", "loose"),
    ("confederated state", "confederated state"),
    ("unitary state", "unitary state"),
    ("nominal", "nominal"),
    ("quasi-polity", "quasi-polity"),
    ("none", "none"),
    ("unknown", "unknown"),
    ("uncoded", "uncoded"),
)

POLITY_CONSECUTIVE_ENTITY_CHOICES = (
    ("continuity", "continuity"),
    ("elite migration", "elite migration"),
    ("cultural assimilation", "cultural assimilation"),
    ("continuation", "continuation"),
    ("indigenous revolt", "indigenous revolt"),
    ("replacement", "replacement"),
    ("population migration", "population migration"),
    ("hostile", "hostile"),
    ("disruption/continuity", "disruption/continuity"),
    ("continuity/discontinuity", "continuity/discontinuity"),
    ("NO_VALUE_ON_WIKI", "NO_VALUE_ON_WIKI"),
    ("suspected unknown", "suspected unknown"),
    ("vassalage", "vassalage"),
    ("not applicable", "not applicable"),
    ("unknown", "unknown"),
    ("economic displacement", "economic displacement"),
    ("secession", "secession"),
)

POLITY_SUPRAPOLITY_RELATIONS_CHOICES = (
    ("vassalage", "vassalage to"),
    ("alliance", "alliance with"),
    ("nominal allegiance", "nominal allegiance to"),
    ("personal union", "personal union with"),
    ("unknown", "unknown"),
    ("uncoded", "uncoded"),
    ("none", "none"),
)

POLITY_RELIGION_GENUS_CHOICES = (
    ("Zoroastrianism", "Zoroastrianism"),
    ("Graeco-Bactrian Religions", "Graeco-Bactrian Religions"),
    ("Buddhism", "Buddhism"),
    ("Christianity", "Christianity"),
    ("Islam", "Islam"),
    ("Mongolian Shamanism", "Mongolian Shamanism"),
    ("Hittite Religions", "Hittite Religions"),
    ("Ismaili", "Ismaili"),
    ("Lydian Religions", "Lydian Religions"),
    ("Chinese State Religion", "Chinese State Religion"),
    ("Egyptian Religions", "Egyptian Religions"),
    ("Ancient Iranian Religions", "Ancient Iranian Religions"),
    ("Hellenistic Religions", "Hellenistic Religions"),
    ("Hephthalite Religions", "Hephthalite Religions"),
    ("Manichaeism", "Manichaeism"),
    ("Ancient East Asian Religion", "Ancient East Asian Religion"),
    ("Jain Traditions", "Jain Traditions"),
    ("Xiongnu Religions", "Xiongnu Religions"),
    ("Roman State Religions", "Roman State Religions"),
    ("Shinto", "Shinto"),
    ("Phrygian Religions", "Phrygian Religions"),
    ("Mesopotamian Religions", "Mesopotamian Religions"),
    ("Hinduism", "Hinduism"),
    ("Ancient Javanese Religions", "Ancient Javanese Religions"),
    ("Confucianism", "Confucianism"),
)

POLITY_RELIGION_FAMILY_CHOICES = (
    ("Saivist Traditions", "Saivist Traditions"),
    ("Assyrian Religions", "Assyrian Religions"),
    ("Republican Religions", "Republican Religions"),
    ("Imperial Confucian Traditions", "Imperial Confucian Traditions"),
    ("Shii", "Shii"),
    ("Bhagavatist Traditions", "Bhagavatist Traditions"),
    ("Sunni", "Sunni"),
    ("Vedist Traditions", "Vedist Traditions"),
    ("Saivist", "Saivist"),
    ("Islam", "Islam"),
    ("Chinese Folk Religion", "Chinese Folk Religion"),
    ("Semitic", "Semitic"),
    ("Vaisnava Traditions", "Vaisnava Traditions"),
    ("Ptolemaic Religion", "Ptolemaic Religion"),
    ("Vedic Traditions", "Vedic Traditions"),
    ("Japanese Buddhism", "Japanese Buddhism"),
    ("Orthodox", "Orthodox"),
    ("Vaishnava Traditions", "Vaishnava Traditions"),
    ("Shang Religion", "Shang Religion"),
    ("Atenism", "Atenism"),
    ("Mahayana", "Mahayana"),
    ("suspected unknown", "suspected unknown"),
    ("Japanese State Shinto", "Japanese State Shinto"),
    ("Saiva Traditions", "Saiva Traditions"),
    ("Sufi", "Sufi"),
    ("Chinese Buddhist Traditions", "Chinese Buddhist Traditions"),
    ("Arian", "Arian"),
    ("Shia", "Shia"),
    ("Catholic", "Catholic"),
    ("Western Zhou Religion", "Western Zhou Religion"),
    ("Imperial Cult", "Imperial Cult"),
    ("Theravada", "Theravada"),
    ("Seleucid Religion", "Seleucid Religion"),
    ("Saivite Hinduism", "Saivite Hinduism"),
    ("Theravada Buddhism", "Theravada Buddhism"),
    ("Theravāda Buddhism", "Theravāda Buddhism"),
    ("Protestant Christianity", "Protestant Christianity"),
    ("Saivist Hinduism", "Saivist Hinduism"),
    ("Sunni Islam", "Sunni Islam"),
    ("Shia Islam", "Shia Islam"),
    ("Vodun", "Vodun"),
    ("Dahomey royal ancestor cult", "Dahomey royal ancestor cult"),
    ("Shaivist", "Shaivist"),
    ("Shaivism", "Shaivism"),
    ("Sufi Islam", "Sufi Islam"),
    ("Shaivite Hinduism", "Shaivite Hinduism"),
    ("Vaishnavist Hinduism", "Vaishnavist Hinduism"),
    ("Catholicism", "Catholicism"),
    ("Protestant", "Protestant"),
    ("Christianity", "Christianity"),
    ("Vedic", "Vedic"),
    ("Church of England", "Church of England"),
    ("Protestantism", "Protestantism"),
    ("Zoroastrianism", "Zoroastrianism"),
    ("Central Asian Shamanism", "Central Asian Shamanism"),
    ("Hawaiian Religion", "Hawaiian Religion"),
    ("Paganism", "Paganism"),
)

POLITY_RELIGION_CHOICES = (
    ("Islam", "Islam"),
    ("Shadhil", "Shadhil"),
    ("Karrami", "Karrami"),
    ("Hanafi", "Hanafi"),
    ("Mevlevi", "Mevlevi"),
    ("Ismaili", "Ismaili"),
    ("Shafii", "Shafii"),
    ("Shia", "Shia"),
    ("Twelver", "Twelver"),
    ("Byzantine Orthodox", "Byzantine Orthodox"),
    ("Bektasi", "Bektasi"),
    ("NO_VALUE_ON_WIKI", "NO_VALUE_ON_WIKI"),
    ("Sunni", "Sunni"),
    ("Roman Catholic", "Roman Catholic"),
)

POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES = (
    ("continuity", "continuity"),
    ("elite migration", "elite migration"),
    ("cultural assimilation", "cultural assimilation"),
    ("continuation", "continuation"),
    ("indigenous revolt", "indigenous revolt"),
    ("replacement", "replacement"),
    ("population migration", "population migration"),
    ("hostile", "hostile"),
    ("disruption/continuity", "disruption/continuity"),
    ("continuity/discontinuity", "continuity/discontinuity"),
    ("NO_VALUE_ON_WIKI", "NO_VALUE_ON_WIKI"),
    ("suspected unknown", "suspected unknown"),
    ("vassalage", "vassalage"),
    ("not applicable", "not applicable"),
    ("unknown", "unknown"),
    ("economic displacement", "economic displacement"),
    ("secession", "secession"),
)


# TUPLE CHOICES THAT ARE THE SAME
POLITY_ALTERNATE_RELIGION_GENUS_CHOICES = POLITY_RELIGION_GENUS_CHOICES
POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES = POLITY_RELIGION_FAMILY_CHOICES
POLITY_ALTERNATE_RELIGION_CHOICES = POLITY_RELIGION_CHOICES

# Create nice constants for the inner fields for downloads
INNER_POLITY_DEGREE_OF_CENTRALIZATION_CHOICES = [
    x[0] for x in POLITY_DEGREE_OF_CENTRALIZATION_CHOICES
]
INNER_POLITY_SUPRAPOLITY_RELATIONS_CHOICES = [
    x[0] for x in POLITY_SUPRAPOLITY_RELATIONS_CHOICES
]
INNER_POLITY_LANGUAGE_CHOICES = [x[0] for x in POLITY_RELIGION_GENUS_CHOICES]
INNER_POLITY_LINGUISTIC_FAMILY_CHOICES = [x[0] for x in POLITY_RELIGION_FAMILY_CHOICES]
INNER_POLITY_LANGUAGE_GENUS_CHOICES = [x[0] for x in POLITY_RELIGION_CHOICES]
INNER_POLITY_RELIGION_GENUS_CHOICES = [x[0] for x in POLITY_RELIGION_GENUS_CHOICES]
INNER_POLITY_RELIGION_FAMILY_CHOICES = [x[0] for x in POLITY_RELIGION_FAMILY_CHOICES]
INNER_POLITY_RELIGION_CHOICES = [x[0] for x in POLITY_RELIGION_CHOICES]
INNER_POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES = [
    x[0] for x in POLITY_RELATIONSHIP_TO_PRECEDING_ENTITY_CHOICES
]
INNER_POLITY_ALTERNATE_RELIGION_GENUS_CHOICES = [
    x[0] for x in POLITY_ALTERNATE_RELIGION_GENUS_CHOICES
]
INNER_POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES = [
    x[0] for x in POLITY_ALTERNATE_RELIGION_FAMILY_CHOICES
]
INNER_POLITY_ALTERNATE_RELIGION_CHOICES = [
    x[0] for x in POLITY_ALTERNATE_RELIGION_CHOICES
]
