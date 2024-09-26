__all__ = [
    "HUMAN_SACRIFICE_HUMAN_SACRIFICE_CHOICES",
    "CRISISDB_CHOICES",
    "SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES",
    "MAGNITUDE_DISEASE_OUTBREAK_CHOICES",
    "DURATION_DISEASE_OUTBREAK_CHOICES",
    "US_STATE_CHOICES",
    "ATTENTION_TAGS_CHOICES",
    "VIOLENCE_TYPE_CHOICES",
    "ALL_VARS_IN_SECTIONS",
    "ALL_VARS_WITH_HIERARCHY",
    "CRISIS_DEFS_EXAMPLES",
    "POWER_TRANSITIONS_DEFS_EXAMPLES",
    "TAGS_DIC",
    "NO_SECTION_DICT",
    "QING_VARS"
]

from ..constants import ICONS, ATTRS_HTML

HUMAN_SACRIFICE_HUMAN_SACRIFICE_CHOICES = (
    ("U", "Unknown"),
    ("P", "Present"),
    ("A~P", "Transitional (Absent -> Present)"),
    ("A", "Absent"),
    ("P~A", "Transitional (Present -> Absent)"),
)

CRISISDB_CHOICES = (
    ("U", "Unknown"),
    ("SU", "Suspected Unknown"),
    ("P", "Present"),
    ("A", "Absent"),
    ("IP", "Inferred Present"),
    ("IA", "Inferred Absent"),
    ("DIS", "Disputed"),
)

SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES = (
    ("Peculiar Epidemics", "Peculiar Epidemics"),
    ("Pestilence", "Pestilence"),
    ("Miasm", "Miasm"),
    ("Pox", "Pox"),
    ("Uncertain Pestilence", "Uncertain Pestilence"),
    ("Dysentery", "Dysentery"),
    ("Malaria", "Malaria"),
    ("Influenza", "Influenza"),
    ("Cholera", "Cholera"),
    ("Diptheria", "Diptheria"),
    ("Plague", "Plague"),
)

MAGNITUDE_DISEASE_OUTBREAK_CHOICES = (
    ("Uncertain", "Uncertain"),
    ("Light", "Light"),
    ("Heavy", "Heavy"),
    ("No description", "No description"),
    ("Heavy- Multiple Times", "Heavy- Multiple Times"),
    ("No Happening", "No Happening"),
    ("Moderate", "Moderate"),
)

DURATION_DISEASE_OUTBREAK_CHOICES = (
    ("No description", "No description"),
    ("Over 90 Days", "Over 90 Days"),
    ("Uncertain", "Uncertain"),
    ("30-60 Days", "30-60 Days"),
    ("1-10 Days", "1-10 Days"),
    ("60-90 Days", "60-90 Days"),
)

US_STATE_CHOICES = (
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
    ("UNK", "UNKNOWN"),
)

ATTENTION_TAGS_CHOICES = (
    ("NeedsExpertInput", "Needs Expert Input"),
    ("IsInconsistent", "Is Inconsistent"),
    ("IsWrong", "Is Wrong"),
    ("IsOk", "IS OK"),
)

VIOLENCE_TYPE_CHOICES = (
    ("lynching", "lynching"),
    ("riot", "riot"),
    ("executions", "executions"),
    ("war", "war"),
    ("assassination", "assassination"),
    ("compilation", "compilation"),
    ("terrorism", "terrorism"),
    ("insurrection", "insurrection"),
    ("mass suicide", "mass suicide"),
    ("unknown", "unknown"),
    ("revenge", "revenge"),
)

ALL_VARS_IN_SECTIONS = {
    "finances": {
        "total_tax": "Total Tax",
        "salt_tax": "Salt Tax",
        "total_revenue": "Total Revenue",
    },
    "goodies": {"bad_boy": "chips", "worse_boy": "cookie eater"},
}

ALL_VARS_WITH_HIERARCHY = {
    "Economy Variables": {
        "Productivity": [
            "agricultural_population",
            "arable_land",
            "arable_land_per_farmer",
            "gross_grain_shared_per_agricultural_population",
            "net_grain_shared_per_agricultural_population",
            "surplus",
            "gdp_per_capita",
        ],
        "State Finances": [
            "military_expense",
            "silver_inflow",
            "silver_stock",
        ],
    },
    "Social Complexity Variables": {"Social Scale": ["total_population"]},
    "Well Being": {
        "Biological Well-Being": [
            "drought_event",
            "locust_event",
            "socioeconomic_turmoil_event",
            "crop_failure_event",
            "famine_event",
            "disease_outbreak",
        ]
    },
}

CRISIS_DEFS_EXAMPLES = {
    "decline": f"""
        <p {ATTRS_HTML.text_secondary}>
            {ICONS.caret_right} Significant population decline (a loose guide is <span {ATTRS_HTML.text_green_bold}>a loss of roughly >10%</span> of total population) which may be caused by factors such as natural disasters, epidemic, famine, or ongoing warfare. Specify the extent of the decline where possible.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: During the Ayyubid Sultanate of 1200 there was a devastating famine which forced some parts of the population into cannibalism.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "collapse": f"""
        <p {ATTRS_HTML.text_secondary}>
            <span {ATTRS_HTML.text_green_bold}>Severe decline (e.g., >50%)</span> or dissolution of a population to a point where it is unable to recover. Specify the extent of the collapse of the population where possible. Generally this involves ‘extinction’ or near-extinction of ethnic, linguistic, or other cultural groups.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The Inca Empire suffered catastrophic losses due to the outbreak of smallpox which was quickly followed by the Spanish conquest. The population was approximately 9 million in 1520 before the arrival of the Spanish and fell to 600,000 by 1620.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "epidemic": f"""
        <p {ATTRS_HTML.text_secondary}>
            Severe outbreak of infectious disease which affects a large portion of the population, such as plague, cholera or smallpox. If estimates or exact figures of those infected or killed are known, specify them.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  In 1596 Habsburg Spain suffered a plague which spread across the entire of mainland Spain and killed an estimated 500,000 people in six years.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "downward_mobility": f"""
        <p {ATTRS_HTML.text_secondary}>
            This refers to the downward mobility - such as loss of power, land, title or privilege - among a large portion of the elite and often their supporters. Events concerning an individual, such as a royal family member being exiled, are not considered here.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: After the Genpei Civil War in 1185 all members of the Minamoto clan were removed from their posts at court and exiled.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "extermination": f"""
        <p {ATTRS_HTML.text_secondary}>
            The mass killing and/or expulsion of an elite group such as a clan or a ruler and their noble supporters. The end of a dynasty is not included here unless it was accompanied by the slaughter of a specific elite group.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: Following the Genkō Civil War in 1333, the entire of the Hōjō clan were forced to commit suicide by the reinstated emperor, Go-Daigo.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "uprising": f"""
        <p {ATTRS_HTML.text_secondary}>
            [NB: formerly "Revolution"]. Widespread serious revolt, rebellion, coup d’etat, or uprising which is often violent (but need not be led by armed groups) and/or leads to significant institutional changes in the polity. Note where possible if uprising is led by elites, military officials, popular / laborer groups (rural or urban), or a combination.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The Mexican War of Independence 1810-1821 was a series of simultaneous regional and local armed conflicts against Spanish rule, which led to the break from Spain and the establishment of the Mexican Empire.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "revolution": f"""
        <p {ATTRS_HTML.text_secondary}>
            Revolution is the attempted forcible overthrow of a government through mass mobilization (whether military or civilian or both) in the name of social justice, inclduing national liberation or ethno-nationalist movements, to create new political institutions. This is distinct from rebeliions and other uprisings that do not necesarrily involve mass mobilization or seek systemic / governmental change (though they can). Revolutions is thus here viewed as a special type of Uprising. These definitions follow: Goldstone 2014 Revolutions: A Very Short Introduction | Goldstone, Jack A., Leonid Grinin, and Andrey Korotayev. Handbook of Revolutions in the 21st Century: The New Waves of Revolutions, and the Causes and Effects of Disruptive Political Change. Springer Nature, 2022.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The failed Czech / Bohemian revolts of during the 30 Years War sought to liberate the territory from Habsburg control and reject Catholic influence .
        </p>""",  # noqa: E501 pylint: disable=C0301
    "successful_revolution": f"""
        <p {ATTRS_HTML.text_secondary}>
            A revolution that succeeds in overthrowing the existing ruler / governmental systems and/or creating a new independent polity.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: French Revolution of 1789 was an elite-led mass mobilization leading to the overthrow of the French Monarchy.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "civil_war": f"""
        <p {ATTRS_HTML.text_secondary}>
            A violent conflict between citizens of the same polity, usually between the state and one or more organized groups, or between two or more organized groups following state collapse.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: In 1727 upon the death of Sultan Isma&rsquo;il of the Alaouite Dynasty, a succession crisis between his sons led to factions within court and the country went to war until 1757.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "century_plus": f"""
        <p {ATTRS_HTML.text_secondary}>
            Any crisis which lasts for a century or more. This may be a string of events such as uprisings, war, and disease during the crisis period rather than one long event.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  In Crete during the late fourth century constant elite in-fighting led to a near-collapse of the aristocratic order and constant warfare, which lasted for hundreds of years, between the city states of Gortyn, Kydonia (Chania), Lyttos, Polyrrhenia and Knossos weakened Crete&rsquo;s economy.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "fragmentation": f"""
        <p {ATTRS_HTML.text_secondary}>
            The division of part, or all, of a polity and its territories into quasi-polities or independent states.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: During the civil wars of the State of Jin in the 5th-and-6th centuries BCE, the Han, Wei and Zhao clans formed an alliance to defeat the more powerful Zhi clan. This resulted in the Partition of Jin in 453 BCE whereby Zhi lands and the rest of Jin were divided between the three successor states who were later known as the Three Jins.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "capital": f"""
        <p {ATTRS_HTML.text_secondary}>
            If the state loses control of capital settlement or the capital is destroyed. If it is destroyed, note whether it was at the hands of internal or external forces.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  In 1115-16 northern tribes attacked the ancient Mexican city of Tula (Tollan), defeated the priest-king, and drove him and his supporters out of the city.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "conquest": f"""
        <p {ATTRS_HTML.text_secondary}>
            The conquest and seizure of the polity’s territory by an external force. This could be a significant part of the territory, a city, the capital, or the entire territory.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: In 1517 the Ottoman forces defeated the Mamluks and seized the sultanate capital of Cairo in Egypt which completed their conquest of the entire Middle East.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "assassination": f"""
        <p {ATTRS_HTML.text_secondary}>
            The murder of the ruler of the polity for ideological or political reasons rather than, for example, if they fall in battle. State the type of assassination if possible, such as execution or poisoning, and who ordered or carried out the assassination if known or speculated.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: When Emperor Ping of the Western Han Empire came of age in 5 BCE and made it clear that he resented the regent Duke Wang Mang&rsquo;s former actions, Mang had the emperor poisoned, and arranged for a distant 1 year old relative to be placed on the throne so that he could control him.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "depose": f"""
        <p {ATTRS_HTML.text_secondary}>
            The ruler of the polity is removed, but not killed. Note: this does not include episodes where the ruler is captured by a foreign polity, but refers to cases where the ruler is removed by ‘internal’ foes.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: During the Eastern Jin Dynasty in 372 CE a powerful general plotted to depose the emperor Fei by spreading damaging rumours of impotency and homosexuality and finally forced Empress Dowager Chu to issue an edict deposing Fei.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "constitution": f"""
        <p {ATTRS_HTML.text_secondary}>
            Major constitutional or institutional change such as how rulers gain power or the role of advisory bodies. This includes both increase or loss of &lsquo;democratic&rsquo; or representative governance, such as the transition from representative oligarchy to dictatorship. It also includes a significant shift in political organization such as the reorganization of provinces, new ideas about kingship, or reforms are included.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The Persian Constitutional Revolution of 1906 led to wide-reaching reforms including the establishment of a parliament and elections, and making the power of the Shah contingent to the will of the people, which saw the beginning of a modern era in Iran.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "religion": f"""
        <p {ATTRS_HTML.text_secondary}>
            The major change or reorganization of religious systems or &lsquo;official cult&rsquo; (the set of collective ritual practices that are most closely associated with legitimation of the power structure). This may be the adoption of a new state religion or state support for a particular religious group.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  After the Islamic Almoravid dynasty occupied and acquired the regions of Kawkaw, Takrur, Ghana, and Bornu, local rulers converted to Islam to ensure administrative support, legitimisation, and commercial contacts. While Islam became an imperial cult and the religion of state, most agricultural groups maintained traditional beliefs.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "unfree_labor": f"""
        <p {ATTRS_HTML.text_secondary}>
            Any change to unfree labor laws. Record only positive changes here such as the abolition of or restcrictions on slavery, or the end of serfdom.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: Alexander II freed all in-service serfs and abolished the practice of serfdom in the Emancipation Reform of 1861 in Russia which granted over 23 million people their freedom and the full rights of citizenship in the Russian Empire.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "suffrage": f"""
        <p {ATTRS_HTML.text_secondary}>
            The new inclusion of a group into the polity’s governance. Record only positive changes here such as the right to vote for previously disenfranchised groups.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>:  In the Early Roman Republic, 494 BCE, the plebeians went on strike, refusing to march to war against a coalition of tribes from central Italy. A settlement was reached when Rome&rsquo;s aristocrats extended to the plebeians the right to vote for certain magistrates, known as the Tribunes of the Plebs (essentially the &lsquo;people&rsquo;s magistrates&rsquo;).
        </p>""",  # noqa: E501 pylint: disable=C0301
    "public_goods": f"""
        <p {ATTRS_HTML.text_secondary}>
            Any public welfare programs or system changes which use significant state resources for the benefit of the wider population. This does not include military spending. Record only positive changes here such as improvement of infrastructure, public places of learning, or health care facilities.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: After a smallpox epidemic, the Habsburg ruler, Maria Theresa (r.1740-1780) ordered the opening of an inoculation center in Vienna.
        </p>""",  # noqa: E501 pylint: disable=C0301
    "labor": f"""
        <p {ATTRS_HTML.text_secondary}>
            Significant change in labor policies, protections, or laws. Record only positive changes here such as the introduction of minimum wage, child labour laws, or worker’s compensation.
        </p>
        <p {ATTRS_HTML.text_secondary_italic}>
            <span {ATTRS_HTML.text_green_bold}>Example</span>: The Cotton Mills and Factories Act 1819 in the UK prevented Cotton Mills from employing children under the age of 9-years-old and restricted the working hours of children aged 9-16 years-old to 12 hours per workday.
        </p>""",  # noqa: E501 pylint: disable=C0301
}

POWER_TRANSITIONS_DEFS_EXAMPLES = {
    "contested": "Was it contested for at least 1 year?",
    "overturn": "NO Definition Yet.",
    "predecessor_assassination": "NO Definition Yet.",
    "intra_elite": "NO Definition Yet.",
    "military_revolt": "NO Definition Yet.",
    "popular_uprising": "NO Definition Yet.",
    "separatist_rebellion": "NO Definition Yet.",
    "external_invasion": "NO Definition Yet.",
    "external_interference": "NO Definition Yet.",
}

TAGS_DIC = {
    "TRS": "Evidenced",
    "DSP": "Disputed",
    "SSP": "Suspected",
    "IFR": "Inferred",
    "UNK": "Unknown",
}

INNER_SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES = [
    x[0] for x in SUB_CATEGORY_DISEASE_OUTBREAK_CHOICES
]
INNER_MAGNITUDE_DISEASE_OUTBREAK_CHOICES = [
    x[0] for x in MAGNITUDE_DISEASE_OUTBREAK_CHOICES
]
INNER_DURATION_DISEASE_OUTBREAK_CHOICES = [
    x[0] for x in DURATION_DISEASE_OUTBREAK_CHOICES
]

NO_SECTION_DICT = {
    "myvar": "Z",
}

QING_VARS = {
        "Economy Variables": {
            "Productivity": [
                [
                    "Agricultural population",
                    "agricultural_populations",
                    "agricultural_population-create",
                    "agricultural_population-download",
                    "agricultural_population-metadownload",
                ],
                [
                    "Arable land",
                    "arable_lands",
                    "arable_land-create",
                    "arable_land-download",
                    "arable_land-metadownload",
                ],
                [
                    "Arable land per farmer",
                    "arable_land_per_farmers",
                    "arable_land_per_farmer-create",
                    "arable_land_per_farmer-download",
                    "arable_land_per_farmer-metadownload",
                ],
                [
                    "Gross grain shared per agricultural population",
                    "gross_grain_shared_per_agricultural_populations",
                    "gross_grain_shared_per_agricultural_population-create",
                    "gross_grain_shared_per_agricultural_population-download",
                    "gross_grain_shared_per_agricultural_population-metadownload",
                ],
                [
                    "Net grain shared per agricultural population",
                    "net_grain_shared_per_agricultural_populations",
                    "net_grain_shared_per_agricultural_population-create",
                    "net_grain_shared_per_agricultural_population-download",
                    "net_grain_shared_per_agricultural_population-metadownload",
                ],
                [
                    "Surplus",
                    "surplus",
                    "surplus-create",
                    "surplus-download",
                    "surplus-metadownload",
                ],
                [
                    "Gdp per capita",
                    "gdp_per_capitas",
                    "gdp_per_capita-create",
                    "gdp_per_capita-download",
                    "gdp_per_capita-metadownload",
                ],
            ],
            "State Finances": [
                [
                    "Military expense",
                    "military_expenses",
                    "military_expense-create",
                    "military_expense-download",
                    "military_expense-metadownload",
                ],
                [
                    "Silver inflow",
                    "silver_inflows",
                    "silver_inflow-create",
                    "silver_inflow-download",
                    "silver_inflow-metadownload",
                ],
                [
                    "Silver stock",
                    "silver_stocks",
                    "silver_stock-create",
                    "silver_stock-download",
                    "silver_stock-metadownload",
                ],
            ],
        },
        "Social Complexity Variables": {
            "Social Scale": [
                [
                    "Total population",
                    "total_populations",
                    "total_population-create",
                    "total_population-download",
                    "total_population-metadownload",
                ]
            ]
        },
        "Well Being": {
            "Biological Well-Being": [
                [
                    "Drought event",
                    "drought_events",
                    "drought_event-create",
                    "drought_event-download",
                    "drought_event-metadownload",
                ],
                [
                    "Locust event",
                    "locust_events",
                    "locust_event-create",
                    "locust_event-download",
                    "locust_event-metadownload",
                ],
                [
                    "Socioeconomic turmoil event",
                    "socioeconomic_turmoil_events",
                    "socioeconomic_turmoil_event-create",
                    "socioeconomic_turmoil_event-download",
                    "socioeconomic_turmoil_event-metadownload",
                ],
                [
                    "Crop failure event",
                    "crop_failure_events",
                    "crop_failure_event-create",
                    "crop_failure_event-download",
                    "crop_failure_event-metadownload",
                ],
                [
                    "Famine event",
                    "famine_events",
                    "famine_event-create",
                    "famine_event-download",
                    "famine_event-metadownload",
                ],
                [
                    "Disease outbreak",
                    "disease_outbreaks",
                    "disease_outbreak-create",
                    "disease_outbreak-download",
                    "disease_outbreak-metadownload",
                ],
            ]
        },
    }
