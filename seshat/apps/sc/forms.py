from django import forms

from ..global_constants import (
    _wrap,
    COMMON_FIELDS,
    COMMON_LABELS,
    COMMON_WIDGETS,
    ATTRS,
)

from .models import (
    Ra,
    Polity_territory,
    Polity_population,
    Population_of_the_largest_settlement,
    Settlement_hierarchy,
    Administrative_level,
    Religious_level,
    Military_level,
    Professional_military_officer,
    Professional_soldier,
    Professional_priesthood,
    Full_time_bureaucrat,
    Examination_system,
    Merit_promotion,
    Specialized_government_building,
    Formal_legal_code,
    Judge,
    Court,
    Professional_lawyer,
    Irrigation_system,
    Drinking_water_supply_system,
    Market,
    Food_storage_site,
    Road,
    Bridge,
    Canal,
    Port,
    Mines_or_quarry,
    Mnemonic_device,
    Nonwritten_record,
    Written_record,
    Script,
    Non_phonetic_writing,
    Phonetic_alphabetic_writing,
    Lists_tables_and_classification,
    Calendar,
    Sacred_text,
    Religious_literature,
    Practical_literature,
    History,
    Philosophy,
    Scientific_literature,
    Fiction,
    Article,
    Token,
    Precious_metal,
    Foreign_coin,
    Indigenous_coin,
    Paper_currency,
    Courier,
    Postal_station,
    General_postal_service,
    Communal_building,
    Utilitarian_public_building,
    Other_utilitarian_public_building,
    Symbolic_building,
    Entertainment_building,
    Knowledge_or_information_building,
    Special_purpose_site,
    Ceremonial_site,
    Burial_site,
    Trading_emporia,
    Enclosure,
    Length_measurement_system,
    Area_measurement_system,
    Volume_measurement_system,
    Weight_measurement_system,
    Time_measurement_system,
    Geometrical_measurement_system,
    Other_measurement_system,
    Debt_and_credit_structure,
    Store_of_wealth,
    Source_of_support,
    Occupational_complexity,
    Special_purpose_house,
    Other_special_purpose_site,
    Largest_communication_distance,
    Fastest_individual_communication,
)


COMMON_LABELS = dict(
    COMMON_LABELS,
    **{
        "polity": _wrap("Polity"),
        "description": _wrap("Description"),
    }
)


class RaForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Ra
        fields = COMMON_FIELDS + ["sc_ra"]
        labels = COMMON_LABELS
        widgets = dict(COMMON_WIDGETS, **{"sc_ra": forms.Select(attrs=ATTRS.MB3_ATTRS)})


class Polity_territoryForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_territory
        fields = COMMON_FIELDS + [
            "polity_territory_from",
            "polity_territory_to",
        ]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "polity_territory_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "polity_territory_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Polity_populationForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Polity_population
        fields = COMMON_FIELDS + [
            "polity_population_from",
            "polity_population_to",
        ]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "polity_population_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "polity_population_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Population_of_the_largest_settlementForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Population_of_the_largest_settlement
        fields = COMMON_FIELDS + [
            "population_of_the_largest_settlement_from",
            "population_of_the_largest_settlement_to",
        ]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "population_of_the_largest_settlement_from": forms.NumberInput(
                    attrs=ATTRS.MB3_ATTRS
                ),
                "population_of_the_largest_settlement_to": forms.NumberInput(
                    attrs=ATTRS.MB3_ATTRS
                ),
            }
        )


class Settlement_hierarchyForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Settlement_hierarchy
        fields = COMMON_FIELDS + [
            "settlement_hierarchy_from",
            "settlement_hierarchy_to",
        ]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "settlement_hierarchy_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "settlement_hierarchy_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Administrative_levelForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Administrative_level
        fields = COMMON_FIELDS + [
            "administrative_level_from",
            "administrative_level_to",
        ]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "administrative_level_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "administrative_level_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Religious_levelForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Religious_level
        fields = COMMON_FIELDS + ["religious_level_from", "religious_level_to"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "religious_level_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "religious_level_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Military_levelForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Military_level
        fields = COMMON_FIELDS + ["military_level_from", "military_level_to"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "military_level_from": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
                "military_level_to": forms.NumberInput(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Professional_military_officerForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Professional_military_officer
        fields = COMMON_FIELDS + ["professional_military_officer"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "professional_military_officer": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Professional_soldierForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Professional_soldier
        fields = COMMON_FIELDS + ["professional_soldier"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "professional_soldier": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Professional_priesthoodForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Professional_priesthood
        fields = COMMON_FIELDS + ["professional_priesthood"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "professional_priesthood": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Full_time_bureaucratForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Full_time_bureaucrat
        fields = COMMON_FIELDS + ["full_time_bureaucrat"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "full_time_bureaucrat": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Examination_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Examination_system
        fields = COMMON_FIELDS + ["examination_system"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "examination_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Merit_promotionForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Merit_promotion
        fields = COMMON_FIELDS + ["merit_promotion"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "merit_promotion": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Specialized_government_buildingForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Specialized_government_building
        fields = COMMON_FIELDS + ["specialized_government_building"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "specialized_government_building": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Formal_legal_codeForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Formal_legal_code
        fields = COMMON_FIELDS + ["formal_legal_code"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "formal_legal_code": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class JudgeForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Judge
        fields = COMMON_FIELDS + ["judge"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "judge": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class CourtForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Court
        fields = COMMON_FIELDS + ["court"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "court": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Professional_lawyerForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Professional_lawyer
        fields = COMMON_FIELDS + ["professional_lawyer"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "professional_lawyer": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Irrigation_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Irrigation_system
        fields = COMMON_FIELDS + ["irrigation_system"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "irrigation_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Drinking_water_supply_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Drinking_water_supply_system
        fields = COMMON_FIELDS + ["drinking_water_supply_system"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "drinking_water_supply_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class MarketForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Market
        fields = COMMON_FIELDS + ["market"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "market": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Food_storage_siteForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Food_storage_site
        fields = COMMON_FIELDS + ["food_storage_site"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "food_storage_site": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class RoadForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Road
        fields = COMMON_FIELDS + ["road"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "road": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class BridgeForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Bridge
        fields = COMMON_FIELDS + ["bridge"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "bridge": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class CanalForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Canal
        fields = COMMON_FIELDS + ["canal"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "canal": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class PortForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Port
        fields = COMMON_FIELDS + ["port"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "port": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Mines_or_quarryForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Mines_or_quarry
        fields = COMMON_FIELDS + ["mines_or_quarry"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "mines_or_quarry": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Mnemonic_deviceForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Mnemonic_device
        fields = COMMON_FIELDS + ["mnemonic_device"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "mnemonic_device": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Nonwritten_recordForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Nonwritten_record
        fields = COMMON_FIELDS + ["nonwritten_record"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "nonwritten_record": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Written_recordForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Written_record
        fields = COMMON_FIELDS + ["written_record"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "written_record": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class ScriptForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Script
        fields = COMMON_FIELDS + ["script"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "script": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Non_phonetic_writingForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Non_phonetic_writing
        fields = COMMON_FIELDS + ["non_phonetic_writing"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "non_phonetic_writing": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Phonetic_alphabetic_writingForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Phonetic_alphabetic_writing
        fields = COMMON_FIELDS + ["phonetic_alphabetic_writing"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "phonetic_alphabetic_writing": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Lists_tables_and_classificationForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Lists_tables_and_classification
        fields = COMMON_FIELDS + ["lists_tables_and_classification"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "lists_tables_and_classification": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class CalendarForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Calendar
        fields = COMMON_FIELDS + ["calendar"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "calendar": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Sacred_textForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Sacred_text
        fields = COMMON_FIELDS + ["sacred_text"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "sacred_text": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Religious_literatureForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Religious_literature
        fields = COMMON_FIELDS + ["religious_literature"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "religious_literature": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Practical_literatureForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Practical_literature
        fields = COMMON_FIELDS + ["practical_literature"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "practical_literature": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class HistoryForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = History
        fields = COMMON_FIELDS + ["history"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "history": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class PhilosophyForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Philosophy
        fields = COMMON_FIELDS + ["philosophy"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "philosophy": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Scientific_literatureForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Scientific_literature
        fields = COMMON_FIELDS + ["scientific_literature"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "scientific_literature": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class FictionForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Fiction
        fields = COMMON_FIELDS + ["fiction"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "fiction": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class ArticleForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Article
        fields = COMMON_FIELDS + ["article"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "article": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class TokenForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Token
        fields = COMMON_FIELDS + ["token"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "token": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Precious_metalForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Precious_metal
        fields = COMMON_FIELDS + ["precious_metal"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "precious_metal": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Foreign_coinForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Foreign_coin
        fields = COMMON_FIELDS + ["foreign_coin"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "foreign_coin": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Indigenous_coinForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Indigenous_coin
        fields = COMMON_FIELDS + ["indigenous_coin"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "indigenous_coin": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Paper_currencyForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Paper_currency
        fields = COMMON_FIELDS + ["paper_currency"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "paper_currency": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class CourierForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Courier
        fields = COMMON_FIELDS + ["courier"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "courier": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Postal_stationForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Postal_station
        fields = COMMON_FIELDS + ["postal_station"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "postal_station": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class General_postal_serviceForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = General_postal_service
        fields = COMMON_FIELDS + ["general_postal_service"]
        labels = COMMON_LABELS
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "general_postal_service": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


# NEW SC vars
class Communal_buildingForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Communal_building
        fields = COMMON_FIELDS + ["communal_building"]
        labels = dict(
            COMMON_LABELS, **{"communal_building": _wrap("Communal Building")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "communal_building": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Utilitarian_public_buildingForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Utilitarian_public_building
        fields = COMMON_FIELDS + ["utilitarian_public_building"]
        labels = dict(
            COMMON_LABELS,
            **{
                "utilitarian_public_building": _wrap("Utilitarian Public Building")
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "utilitarian_public_building": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Other_utilitarian_public_buildingForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Other_utilitarian_public_building
        fields = COMMON_FIELDS + ["other_utilitarian_public_building"]
        labels = dict(
            COMMON_LABELS,
            **{
                "other_utilitarian_public_building": _wrap("Other Utilitarian Public Building")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "other_utilitarian_public_building": forms.Select(
                    attrs=ATTRS.MB3_ATTRS
                ),
            }
        )


class Symbolic_buildingForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Symbolic_building
        fields = COMMON_FIELDS + ["symbolic_building"]
        labels = dict(
            COMMON_LABELS, **{"symbolic_building": _wrap("Symbolic Building")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "symbolic_building": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Entertainment_buildingForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Entertainment_building
        fields = COMMON_FIELDS + ["entertainment_building"]
        labels = dict(
            COMMON_LABELS,
            **{"entertainment_building": _wrap("Entertainment Building")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "entertainment_building": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Knowledge_or_information_buildingForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Knowledge_or_information_building
        fields = COMMON_FIELDS + ["knowledge_or_information_building"]
        labels = dict(
            COMMON_LABELS,
            **{
                "knowledge_or_information_building": _wrap("Knowledge Or Information Building")  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "knowledge_or_information_building": forms.Select(
                    attrs=ATTRS.MB3_ATTRS
                ),
            }
        )


class Special_purpose_siteForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Special_purpose_site
        fields = COMMON_FIELDS + ["special_purpose_site"]
        labels = dict(
            COMMON_LABELS,
            **{"special_purpose_site": _wrap("Special Purpose Site")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "special_purpose_site": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Ceremonial_siteForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Ceremonial_site
        fields = COMMON_FIELDS + ["ceremonial_site"]
        labels = dict(
            COMMON_LABELS, **{"ceremonial_site": _wrap("Ceremonial Site")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "ceremonial_site": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Burial_siteForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Burial_site
        fields = COMMON_FIELDS + ["burial_site"]
        labels = dict(COMMON_LABELS, **{"burial_site": _wrap("Burial Site")})
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "burial_site": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Trading_emporiaForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Trading_emporia
        fields = COMMON_FIELDS + ["trading_emporia"]
        labels = dict(
            COMMON_LABELS, **{"trading_emporia": _wrap("Trading Emporia")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "trading_emporia": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class EnclosureForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Enclosure
        fields = COMMON_FIELDS + ["enclosure"]
        labels = dict(COMMON_LABELS, **{"enclosure": _wrap("Enclosure")})
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "enclosure": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Length_measurement_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Length_measurement_system
        fields = COMMON_FIELDS + ["length_measurement_system"]
        labels = dict(
            COMMON_LABELS,
            **{"length_measurement_system": _wrap("Length Measurement System")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "length_measurement_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Area_measurement_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Area_measurement_system
        fields = COMMON_FIELDS + ["area_measurement_system"]
        labels = dict(
            COMMON_LABELS,
            **{"area_measurement_system": _wrap("Area Measurement System")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "area_measurement_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Volume_measurement_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Volume_measurement_system
        fields = COMMON_FIELDS + ["volume_measurement_system"]
        labels = dict(
            COMMON_LABELS,
            **{"volume_measurement_system": _wrap("Area Measurement System")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "volume_measurement_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Weight_measurement_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Weight_measurement_system
        fields = COMMON_FIELDS + ["weight_measurement_system"]
        labels = dict(
            COMMON_LABELS,
            **{"weight_measurement_system": _wrap("Weight Measurement System")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "weight_measurement_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Time_measurement_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Time_measurement_system
        fields = COMMON_FIELDS + ["time_measurement_system"]
        labels = dict(
            COMMON_LABELS,
            **{"time_measurement_system": _wrap("Time Measurement System")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "time_measurement_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Geometrical_measurement_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Geometrical_measurement_system
        fields = COMMON_FIELDS + ["geometrical_measurement_system"]
        labels = dict(
            COMMON_LABELS,
            **{
                "geometrical_measurement_system": _wrap("Geometrical Measurement System")
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "geometrical_measurement_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Other_measurement_systemForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Other_measurement_system
        fields = COMMON_FIELDS + ["other_measurement_system"]
        labels = dict(
            COMMON_LABELS,
            **{"other_measurement_system": _wrap("Other Measurement System")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "other_measurement_system": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Debt_and_credit_structureForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Debt_and_credit_structure
        fields = COMMON_FIELDS + ["debt_and_credit_structure"]
        labels = dict(
            COMMON_LABELS,
            **{"debt_and_credit_structure": _wrap("Debt And Credit Structure")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "debt_and_credit_structure": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Store_of_wealthForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Store_of_wealth
        fields = COMMON_FIELDS + ["store_of_wealth"]
        labels = dict(
            COMMON_LABELS, **{"store_of_wealth": _wrap("Store Of Wealth")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "store_of_wealth": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Source_of_supportForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Source_of_support
        fields = COMMON_FIELDS + ["source_of_support"]
        labels = dict(
            COMMON_LABELS, **{"source_of_support": _wrap("Source Of Support")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "source_of_support": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Occupational_complexityForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Occupational_complexity
        fields = COMMON_FIELDS + ["occupational_complexity"]
        labels = dict(
            COMMON_LABELS,
            **{"occupational_complexity": _wrap("Occupational Complexity")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "occupational_complexity": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Special_purpose_houseForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Special_purpose_house
        fields = COMMON_FIELDS + ["special_purpose_house"]
        labels = dict(
            COMMON_LABELS,
            **{"special_purpose_house": _wrap("Special Purpose House")}
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "special_purpose_house": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Other_special_purpose_siteForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Other_special_purpose_site
        fields = COMMON_FIELDS + ["other_special_purpose_site"]
        labels = dict(
            COMMON_LABELS,
            **{
                "other_special_purpose_site": _wrap("Other Special Purpose Site")
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "other_special_purpose_site": forms.Select(attrs=ATTRS.MB3_ATTRS),
            }
        )


class Largest_communication_distanceForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Largest_communication_distance
        fields = COMMON_FIELDS + [
            "largest_communication_distance_from",
            "largest_communication_distance_to",
        ]
        labels = dict(
            COMMON_LABELS,
            **{
                "largest_communication_distance_from": _wrap("Largest Communication Distance (From)"),  # noqa: E501 pylint: disable=C0301
                "largest_communication_distance_to": _wrap("Largest Communication Distance (To)"),  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "largest_communication_distance_from": forms.NumberInput(
                    attrs=ATTRS.MB3_ATTRS
                ),
                "largest_communication_distance_to": forms.NumberInput(
                    attrs=ATTRS.MB3_ATTRS
                ),
            }
        )


class Fastest_individual_communicationForm(forms.ModelForm):
    """
    TODO: docstring
    """

    class Meta:
        """
        :noindex:
        """

        model = Fastest_individual_communication
        fields = COMMON_FIELDS + [
            "fastest_individual_communication_from",
            "fastest_individual_communication_to",
        ]
        labels = dict(
            COMMON_LABELS,
            **{
                "fastest_individual_communication_from": _wrap("Fastest Individual Communication (From)"),  # noqa: E501 pylint: disable=C0301
                "fastest_individual_communication_to": _wrap("Fastest Individual Communication (To)"),  # noqa: E501 pylint: disable=C0301
            }
        )
        widgets = dict(
            COMMON_WIDGETS,
            **{
                "fastest_individual_communication_from": forms.NumberInput(
                    attrs=ATTRS.MB3_ATTRS
                ),
                "fastest_individual_communication_to": forms.NumberInput(
                    attrs=ATTRS.MB3_ATTRS
                ),
            }
        )
