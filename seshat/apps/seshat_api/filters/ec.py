from django_filters import rest_framework as django_filters
from ._mixins import SeshatCommonFilter


from ..models import (
    Lux_precious_metal,
    Luxury_fabrics,
    Luxury_manufactured_goods,
    Luxury_spices_incense_and_dyes,
    Luxury_drink_alcohol,
    Luxury_glass_goods,
    Lux_fine_ceramic_wares,
    Lux_precious_stone,
    Lux_statuary,
    Luxury_food,
    Other_luxury_personal_items,
)

class BaseLuxFilter(SeshatCommonFilter, django_filters.FilterSet):
    class Meta:
        model = None  # Replace with your specific model when subclassing or registering
        fields = {
            "coded_value": ["exact"],
            "place_of_provenance_pol": ["exact"],
            "place_of_provenance_str": ["icontains"],
            "ruler_consumption": ["exact"],
            "ruler_consumption_tag": ["exact"],
            "elite_consumption": ["exact"],
            "elite_consumption_tag": ["exact"],
            "common_people_consumption": ["exact"],
            "common_people_consumption_tag": ["exact"],
        }

class LuxPreciousMetalFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Lux_precious_metal

class LuxuryFabricsFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Luxury_fabrics

class LuxuryManufacturedGoodsFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Luxury_manufactured_goods

class LuxurySpicesIncenseAndDyesFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Luxury_spices_incense_and_dyes

class LuxuryDrinkAlcoholFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Luxury_drink_alcohol

class LuxuryGlassGoodsFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Luxury_glass_goods

class LuxFineCeramicWaresFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Lux_fine_ceramic_wares

class LuxPreciousStoneFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Lux_precious_stone

class LuxStatuaryFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Lux_statuary

class LuxuryFoodFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Luxury_food

class OtherLuxuryPersonalItemsFilter(BaseLuxFilter):
    class Meta(BaseLuxFilter.Meta):
        model = Other_luxury_personal_items
