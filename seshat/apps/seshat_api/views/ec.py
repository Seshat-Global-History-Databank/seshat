from rest_framework import viewsets

from ._mixins import (
    FilterBackends,
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    MixinLuxuryGoodsSeshatAPISerializer,
    SeshatAPIPagination,
)

from ..filters.ec import (
    LuxPreciousMetalFilter,
    LuxuryFabricsFilter,
    LuxuryManufacturedGoodsFilter,
    LuxurySpicesIncenseAndDyesFilter,
    LuxuryDrinkAlcoholFilter,
    LuxuryGlassGoodsFilter,
    LuxFineCeramicWaresFilter,
    LuxPreciousStoneFilter,
    LuxStatuaryFilter,
    LuxuryFoodFilter,
    OtherLuxuryPersonalItemsFilter,
)

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


class LuxPreciousMetalViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Lux_precious_metal
    pagination_class = SeshatAPIPagination
    filterset_class = LuxPreciousMetalFilter


class LuxuryFabricsViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Luxury_fabrics
    pagination_class = SeshatAPIPagination
    filterset_class = LuxuryFabricsFilter


class LuxuryManufacturedGoodsViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Luxury_manufactured_goods
    pagination_class = SeshatAPIPagination
    filterset_class = LuxuryManufacturedGoodsFilter


class LuxurySpicesIncenseAndDyesViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Luxury_spices_incense_and_dyes
    pagination_class = SeshatAPIPagination
    filterset_class = LuxurySpicesIncenseAndDyesFilter


class LuxuryDrinkAlcoholViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Luxury_drink_alcohol
    pagination_class = SeshatAPIPagination
    filterset_class = LuxuryDrinkAlcoholFilter


class LuxuryGlassGoodsViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Luxury_glass_goods
    pagination_class = SeshatAPIPagination
    filterset_class = LuxuryGlassGoodsFilter


class LuxFineCeramicWaresViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Lux_fine_ceramic_wares
    pagination_class = SeshatAPIPagination
    filterset_class = LuxFineCeramicWaresFilter


class LuxPreciousStoneViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Lux_precious_stone
    pagination_class = SeshatAPIPagination
    filterset_class = LuxPreciousStoneFilter


class LuxStatuaryViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Lux_statuary
    pagination_class = SeshatAPIPagination
    filterset_class = LuxStatuaryFilter


class LuxuryFoodViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Luxury_food
    pagination_class = SeshatAPIPagination
    filterset_class = LuxuryFoodFilter


class OtherLuxuryPersonalItemsViewSet(
    FilterBackends,
    MixinLuxuryGoodsSeshatAPISerializer,
    MixinSeshatAPIAuth,
    viewsets.ModelViewSet,
):
    model = Other_luxury_personal_items
    pagination_class = SeshatAPIPagination
    filterset_class = OtherLuxuryPersonalItemsFilter
