from django.urls import path

from . import views


urlpatterns = [
    path('wfvars/', views.wfvars, name='wfvars'),
        path('download-csv-wf-all/', views.download_csv_all_wf,name='download_csv_all_wf'),
     path('problematic_wf_data_table/', views.show_problematic_wf_data_table, name='problematic_wf_data_table'),

]

urlpatterns += [
     path('download_csv_fortifications/', views.download_csv_fortifications,name='download_csv_fortifications'),
     path('download_csv_military_use_of_metals/', views.download_csv_military_use_of_metals,name='download_csv_military_use_of_metals'),
     path('download_csv_projectiles/', views.download_csv_projectiles,name='download_csv_projectiles'),
     path('download_csv_handheld_weapons/', views.download_csv_handheld_weapons,name='download_csv_handheld_weapons'),
     path('download_csv_animals_used_in_warfare/', views.download_csv_animals_used_in_warfare,name='download_csv_animals_used_in_warfare'),
     path('download_csv_armor/', views.download_csv_armor,name='download_csv_armor'),
     path('download_csv_naval_technology/', views.download_csv_naval_technology,name='download_csv_naval_technology'),


]

urlpatterns += [
    path('long_wall/create/', views.Long_wallCreate.as_view(),
         name="long_wall-create"),

    path('long_walls/', views.Long_wallListView.as_view(), name='long_walls'),
    path('long_walls_all/', views.Long_wallListViewAll.as_view(), name='long_walls_all'),
    path('long_wall/<int:pk>', views.Long_wallDetailView.as_view(),
         name='long_wall-detail'),
    path('long_wall/<int:pk>/update/',
         views.Long_wallUpdate.as_view(), name="long_wall-update"),
    path('long_wall/<int:pk>/delete/',
         views.Long_wallDelete.as_view(), name="long_wall-delete"),
    # Download
    path('long_walldownload/', views.long_wall_download,
         name="long_wall-download"),
    path('long_wallmetadownload/', views.long_wall_meta_download,
         name="long_wall-metadownload"),
]
    


urlpatterns += [
    path('copper/create/', views.CopperCreate.as_view(),
         name="copper-create"),

    path('coppers/', views.CopperListView.as_view(), name='coppers'),
    path('coppers_all/', views.CopperListViewAll.as_view(), name='coppers_all'),
    path('copper/<int:pk>', views.CopperDetailView.as_view(),
         name='copper-detail'),
    path('copper/<int:pk>/update/',
         views.CopperUpdate.as_view(), name="copper-update"),
    path('copper/<int:pk>/delete/',
         views.CopperDelete.as_view(), name="copper-delete"),
    # Download
    path('copperdownload/', views.copper_download,
         name="copper-download"),
    path('coppermetadownload/', views.copper_meta_download,
         name="copper-metadownload"),
]
        

urlpatterns += [
    path('bronze/create/', views.BronzeCreate.as_view(),
         name="bronze-create"),

    path('bronzes/', views.BronzeListView.as_view(), name='bronzes'),
    path('bronzes_all/', views.BronzeListViewAll.as_view(), name='bronzes_all'),
    path('bronze/<int:pk>', views.BronzeDetailView.as_view(),
         name='bronze-detail'),
    path('bronze/<int:pk>/update/',
         views.BronzeUpdate.as_view(), name="bronze-update"),
    path('bronze/<int:pk>/delete/',
         views.BronzeDelete.as_view(), name="bronze-delete"),
    # Download
    path('bronzedownload/', views.bronze_download,
         name="bronze-download"),
    path('bronzemetadownload/', views.bronze_meta_download,
         name="bronze-metadownload"),
]
        

urlpatterns += [
    path('iron/create/', views.IronCreate.as_view(),
         name="iron-create"),

    path('irons/', views.IronListView.as_view(), name='irons'),
    path('irons_all/', views.IronListViewAll.as_view(), name='irons_all'),
    path('iron/<int:pk>', views.IronDetailView.as_view(),
         name='iron-detail'),
    path('iron/<int:pk>/update/',
         views.IronUpdate.as_view(), name="iron-update"),
    path('iron/<int:pk>/delete/',
         views.IronDelete.as_view(), name="iron-delete"),
    # Download
    path('irondownload/', views.iron_download,
         name="iron-download"),
    path('ironmetadownload/', views.iron_meta_download,
         name="iron-metadownload"),
]
        

urlpatterns += [
    path('steel/create/', views.SteelCreate.as_view(),
         name="steel-create"),

    path('steels/', views.SteelListView.as_view(), name='steels'),
    path('steels_all/', views.SteelListViewAll.as_view(), name='steels_all'),
    path('steel/<int:pk>', views.SteelDetailView.as_view(),
         name='steel-detail'),
    path('steel/<int:pk>/update/',
         views.SteelUpdate.as_view(), name="steel-update"),
    path('steel/<int:pk>/delete/',
         views.SteelDelete.as_view(), name="steel-delete"),
    # Download
    path('steeldownload/', views.steel_download,
         name="steel-download"),
    path('steelmetadownload/', views.steel_meta_download,
         name="steel-metadownload"),
]
        

urlpatterns += [
    path('javelin/create/', views.JavelinCreate.as_view(),
         name="javelin-create"),

    path('javelins/', views.JavelinListView.as_view(), name='javelins'),
    path('javelins_all/', views.JavelinListViewAll.as_view(), name='javelins_all'),
    path('javelin/<int:pk>', views.JavelinDetailView.as_view(),
         name='javelin-detail'),
    path('javelin/<int:pk>/update/',
         views.JavelinUpdate.as_view(), name="javelin-update"),
    path('javelin/<int:pk>/delete/',
         views.JavelinDelete.as_view(), name="javelin-delete"),
    # Download
    path('javelindownload/', views.javelin_download,
         name="javelin-download"),
    path('javelinmetadownload/', views.javelin_meta_download,
         name="javelin-metadownload"),
]
        

urlpatterns += [
    path('atlatl/create/', views.AtlatlCreate.as_view(),
         name="atlatl-create"),

    path('atlatls/', views.AtlatlListView.as_view(), name='atlatls'),
    path('atlatls_all/', views.AtlatlListViewAll.as_view(), name='atlatls_all'),
    path('atlatl/<int:pk>', views.AtlatlDetailView.as_view(),
         name='atlatl-detail'),
    path('atlatl/<int:pk>/update/',
         views.AtlatlUpdate.as_view(), name="atlatl-update"),
    path('atlatl/<int:pk>/delete/',
         views.AtlatlDelete.as_view(), name="atlatl-delete"),
    # Download
    path('atlatldownload/', views.atlatl_download,
         name="atlatl-download"),
    path('atlatlmetadownload/', views.atlatl_meta_download,
         name="atlatl-metadownload"),
]
        

urlpatterns += [
    path('sling/create/', views.SlingCreate.as_view(),
         name="sling-create"),

    path('slings/', views.SlingListView.as_view(), name='slings'),
    path('slings_all/', views.SlingListViewAll.as_view(), name='slings_all'),
    path('sling/<int:pk>', views.SlingDetailView.as_view(),
         name='sling-detail'),
    path('sling/<int:pk>/update/',
         views.SlingUpdate.as_view(), name="sling-update"),
    path('sling/<int:pk>/delete/',
         views.SlingDelete.as_view(), name="sling-delete"),
    # Download
    path('slingdownload/', views.sling_download,
         name="sling-download"),
    path('slingmetadownload/', views.sling_meta_download,
         name="sling-metadownload"),
]
        

urlpatterns += [
    path('self_bow/create/', views.Self_bowCreate.as_view(),
         name="self_bow-create"),

    path('self_bows/', views.Self_bowListView.as_view(), name='self_bows'),
    path('self_bows_all/', views.Self_bowListViewAll.as_view(), name='self_bows_all'),
    path('self_bow/<int:pk>', views.Self_bowDetailView.as_view(),
         name='self_bow-detail'),
    path('self_bow/<int:pk>/update/',
         views.Self_bowUpdate.as_view(), name="self_bow-update"),
    path('self_bow/<int:pk>/delete/',
         views.Self_bowDelete.as_view(), name="self_bow-delete"),
    # Download
    path('self_bowdownload/', views.self_bow_download,
         name="self_bow-download"),
    path('self_bowmetadownload/', views.self_bow_meta_download,
         name="self_bow-metadownload"),
]
        

urlpatterns += [
    path('composite_bow/create/', views.Composite_bowCreate.as_view(),
         name="composite_bow-create"),

    path('composite_bows/', views.Composite_bowListView.as_view(), name='composite_bows'),
    path('composite_bows_all/', views.Composite_bowListViewAll.as_view(), name='composite_bows_all'),
    path('composite_bow/<int:pk>', views.Composite_bowDetailView.as_view(),
         name='composite_bow-detail'),
    path('composite_bow/<int:pk>/update/',
         views.Composite_bowUpdate.as_view(), name="composite_bow-update"),
    path('composite_bow/<int:pk>/delete/',
         views.Composite_bowDelete.as_view(), name="composite_bow-delete"),
    # Download
    path('composite_bowdownload/', views.composite_bow_download,
         name="composite_bow-download"),
    path('composite_bowmetadownload/', views.composite_bow_meta_download,
         name="composite_bow-metadownload"),
]
        

urlpatterns += [
    path('crossbow/create/', views.CrossbowCreate.as_view(),
         name="crossbow-create"),

    path('crossbows/', views.CrossbowListView.as_view(), name='crossbows'),
    path('crossbows_all/', views.CrossbowListViewAll.as_view(), name='crossbows_all'),
    path('crossbow/<int:pk>', views.CrossbowDetailView.as_view(),
         name='crossbow-detail'),
    path('crossbow/<int:pk>/update/',
         views.CrossbowUpdate.as_view(), name="crossbow-update"),
    path('crossbow/<int:pk>/delete/',
         views.CrossbowDelete.as_view(), name="crossbow-delete"),
    # Download
    path('crossbowdownload/', views.crossbow_download,
         name="crossbow-download"),
    path('crossbowmetadownload/', views.crossbow_meta_download,
         name="crossbow-metadownload"),
]
        

urlpatterns += [
    path('tension_siege_engine/create/', views.Tension_siege_engineCreate.as_view(),
         name="tension_siege_engine-create"),

    path('tension_siege_engines/', views.Tension_siege_engineListView.as_view(), name='tension_siege_engines'),
    path('tension_siege_engines_all/', views.Tension_siege_engineListViewAll.as_view(), name='tension_siege_engines_all'),
    path('tension_siege_engine/<int:pk>', views.Tension_siege_engineDetailView.as_view(),
         name='tension_siege_engine-detail'),
    path('tension_siege_engine/<int:pk>/update/',
         views.Tension_siege_engineUpdate.as_view(), name="tension_siege_engine-update"),
    path('tension_siege_engine/<int:pk>/delete/',
         views.Tension_siege_engineDelete.as_view(), name="tension_siege_engine-delete"),
    # Download
    path('tension_siege_enginedownload/', views.tension_siege_engine_download,
         name="tension_siege_engine-download"),
    path('tension_siege_enginemetadownload/', views.tension_siege_engine_meta_download,
         name="tension_siege_engine-metadownload"),
]
        

urlpatterns += [
    path('sling_siege_engine/create/', views.Sling_siege_engineCreate.as_view(),
         name="sling_siege_engine-create"),

    path('sling_siege_engines/', views.Sling_siege_engineListView.as_view(), name='sling_siege_engines'),
    path('sling_siege_engines_all/', views.Sling_siege_engineListViewAll.as_view(), name='sling_siege_engines_all'),
    path('sling_siege_engine/<int:pk>', views.Sling_siege_engineDetailView.as_view(),
         name='sling_siege_engine-detail'),
    path('sling_siege_engine/<int:pk>/update/',
         views.Sling_siege_engineUpdate.as_view(), name="sling_siege_engine-update"),
    path('sling_siege_engine/<int:pk>/delete/',
         views.Sling_siege_engineDelete.as_view(), name="sling_siege_engine-delete"),
    # Download
    path('sling_siege_enginedownload/', views.sling_siege_engine_download,
         name="sling_siege_engine-download"),
    path('sling_siege_enginemetadownload/', views.sling_siege_engine_meta_download,
         name="sling_siege_engine-metadownload"),
]
        

urlpatterns += [
    path('gunpowder_siege_artillery/create/', views.Gunpowder_siege_artilleryCreate.as_view(),
         name="gunpowder_siege_artillery-create"),

    path('gunpowder_siege_artillerys/', views.Gunpowder_siege_artilleryListView.as_view(), name='gunpowder_siege_artillerys'),
    path('gunpowder_siege_artillerys_all/', views.Gunpowder_siege_artilleryListViewAll.as_view(), name='gunpowder_siege_artillerys_all'),
    path('gunpowder_siege_artillery/<int:pk>', views.Gunpowder_siege_artilleryDetailView.as_view(),
         name='gunpowder_siege_artillery-detail'),
    path('gunpowder_siege_artillery/<int:pk>/update/',
         views.Gunpowder_siege_artilleryUpdate.as_view(), name="gunpowder_siege_artillery-update"),
    path('gunpowder_siege_artillery/<int:pk>/delete/',
         views.Gunpowder_siege_artilleryDelete.as_view(), name="gunpowder_siege_artillery-delete"),
    # Download
    path('gunpowder_siege_artillerydownload/', views.gunpowder_siege_artillery_download,
         name="gunpowder_siege_artillery-download"),
    path('gunpowder_siege_artillerymetadownload/', views.gunpowder_siege_artillery_meta_download,
         name="gunpowder_siege_artillery-metadownload"),
]
        

urlpatterns += [
    path('handheld_firearm/create/', views.Handheld_firearmCreate.as_view(),
         name="handheld_firearm-create"),

    path('handheld_firearms/', views.Handheld_firearmListView.as_view(), name='handheld_firearms'),
    path('handheld_firearms_all/', views.Handheld_firearmListViewAll.as_view(), name='handheld_firearms_all'),
    path('handheld_firearm/<int:pk>', views.Handheld_firearmDetailView.as_view(),
         name='handheld_firearm-detail'),
    path('handheld_firearm/<int:pk>/update/',
         views.Handheld_firearmUpdate.as_view(), name="handheld_firearm-update"),
    path('handheld_firearm/<int:pk>/delete/',
         views.Handheld_firearmDelete.as_view(), name="handheld_firearm-delete"),
    # Download
    path('handheld_firearmdownload/', views.handheld_firearm_download,
         name="handheld_firearm-download"),
    path('handheld_firearmmetadownload/', views.handheld_firearm_meta_download,
         name="handheld_firearm-metadownload"),
]
        

urlpatterns += [
    path('war_club/create/', views.War_clubCreate.as_view(),
         name="war_club-create"),

    path('war_clubs/', views.War_clubListView.as_view(), name='war_clubs'),
    path('war_clubs_all/', views.War_clubListViewAll.as_view(), name='war_clubs_all'),
    path('war_club/<int:pk>', views.War_clubDetailView.as_view(),
         name='war_club-detail'),
    path('war_club/<int:pk>/update/',
         views.War_clubUpdate.as_view(), name="war_club-update"),
    path('war_club/<int:pk>/delete/',
         views.War_clubDelete.as_view(), name="war_club-delete"),
    # Download
    path('war_clubdownload/', views.war_club_download,
         name="war_club-download"),
    path('war_clubmetadownload/', views.war_club_meta_download,
         name="war_club-metadownload"),
]
        

urlpatterns += [
    path('battle_axe/create/', views.Battle_axeCreate.as_view(),
         name="battle_axe-create"),

    path('battle_axes/', views.Battle_axeListView.as_view(), name='battle_axes'),
    path('battle_axes_all/', views.Battle_axeListViewAll.as_view(), name='battle_axes_all'),
    path('battle_axe/<int:pk>', views.Battle_axeDetailView.as_view(),
         name='battle_axe-detail'),
    path('battle_axe/<int:pk>/update/',
         views.Battle_axeUpdate.as_view(), name="battle_axe-update"),
    path('battle_axe/<int:pk>/delete/',
         views.Battle_axeDelete.as_view(), name="battle_axe-delete"),
    # Download
    path('battle_axedownload/', views.battle_axe_download,
         name="battle_axe-download"),
    path('battle_axemetadownload/', views.battle_axe_meta_download,
         name="battle_axe-metadownload"),
]
        

urlpatterns += [
    path('dagger/create/', views.DaggerCreate.as_view(),
         name="dagger-create"),

    path('daggers/', views.DaggerListView.as_view(), name='daggers'),
    path('daggers_all/', views.DaggerListViewAll.as_view(), name='daggers_all'),
    path('dagger/<int:pk>', views.DaggerDetailView.as_view(),
         name='dagger-detail'),
    path('dagger/<int:pk>/update/',
         views.DaggerUpdate.as_view(), name="dagger-update"),
    path('dagger/<int:pk>/delete/',
         views.DaggerDelete.as_view(), name="dagger-delete"),
    # Download
    path('daggerdownload/', views.dagger_download,
         name="dagger-download"),
    path('daggermetadownload/', views.dagger_meta_download,
         name="dagger-metadownload"),
]
        

urlpatterns += [
    path('sword/create/', views.SwordCreate.as_view(),
         name="sword-create"),

    path('swords/', views.SwordListView.as_view(), name='swords'),
    path('swords_all/', views.SwordListViewAll.as_view(), name='swords_all'),
    path('sword/<int:pk>', views.SwordDetailView.as_view(),
         name='sword-detail'),
    path('sword/<int:pk>/update/',
         views.SwordUpdate.as_view(), name="sword-update"),
    path('sword/<int:pk>/delete/',
         views.SwordDelete.as_view(), name="sword-delete"),
    # Download
    path('sworddownload/', views.sword_download,
         name="sword-download"),
    path('swordmetadownload/', views.sword_meta_download,
         name="sword-metadownload"),
]
        

urlpatterns += [
    path('spear/create/', views.SpearCreate.as_view(),
         name="spear-create"),

    path('spears/', views.SpearListView.as_view(), name='spears'),
    path('spears_all/', views.SpearListViewAll.as_view(), name='spears_all'),
    path('spear/<int:pk>', views.SpearDetailView.as_view(),
         name='spear-detail'),
    path('spear/<int:pk>/update/',
         views.SpearUpdate.as_view(), name="spear-update"),
    path('spear/<int:pk>/delete/',
         views.SpearDelete.as_view(), name="spear-delete"),
    # Download
    path('speardownload/', views.spear_download,
         name="spear-download"),
    path('spearmetadownload/', views.spear_meta_download,
         name="spear-metadownload"),
]
        

urlpatterns += [
    path('polearm/create/', views.PolearmCreate.as_view(),
         name="polearm-create"),

    path('polearms/', views.PolearmListView.as_view(), name='polearms'),
    path('polearms_all/', views.PolearmListViewAll.as_view(), name='polearms_all'),
    path('polearm/<int:pk>', views.PolearmDetailView.as_view(),
         name='polearm-detail'),
    path('polearm/<int:pk>/update/',
         views.PolearmUpdate.as_view(), name="polearm-update"),
    path('polearm/<int:pk>/delete/',
         views.PolearmDelete.as_view(), name="polearm-delete"),
    # Download
    path('polearmdownload/', views.polearm_download,
         name="polearm-download"),
    path('polearmmetadownload/', views.polearm_meta_download,
         name="polearm-metadownload"),
]
        

urlpatterns += [
    path('dog/create/', views.DogCreate.as_view(),
         name="dog-create"),

    path('dogs/', views.DogListView.as_view(), name='dogs'),
    path('dogs_all/', views.DogListViewAll.as_view(), name='dogs_all'),
    path('dog/<int:pk>', views.DogDetailView.as_view(),
         name='dog-detail'),
    path('dog/<int:pk>/update/',
         views.DogUpdate.as_view(), name="dog-update"),
    path('dog/<int:pk>/delete/',
         views.DogDelete.as_view(), name="dog-delete"),
    # Download
    path('dogdownload/', views.dog_download,
         name="dog-download"),
    path('dogmetadownload/', views.dog_meta_download,
         name="dog-metadownload"),
]
        

urlpatterns += [
    path('donkey/create/', views.DonkeyCreate.as_view(),
         name="donkey-create"),

    path('donkeys/', views.DonkeyListView.as_view(), name='donkeys'),
    path('donkeys_all/', views.DonkeyListViewAll.as_view(), name='donkeys_all'),
    path('donkey/<int:pk>', views.DonkeyDetailView.as_view(),
         name='donkey-detail'),
    path('donkey/<int:pk>/update/',
         views.DonkeyUpdate.as_view(), name="donkey-update"),
    path('donkey/<int:pk>/delete/',
         views.DonkeyDelete.as_view(), name="donkey-delete"),
    # Download
    path('donkeydownload/', views.donkey_download,
         name="donkey-download"),
    path('donkeymetadownload/', views.donkey_meta_download,
         name="donkey-metadownload"),
]
        

urlpatterns += [
    path('horse/create/', views.HorseCreate.as_view(),
         name="horse-create"),

    path('horses/', views.HorseListView.as_view(), name='horses'),
    path('horses_all/', views.HorseListViewAll.as_view(), name='horses_all'),
    path('horse/<int:pk>', views.HorseDetailView.as_view(),
         name='horse-detail'),
    path('horse/<int:pk>/update/',
         views.HorseUpdate.as_view(), name="horse-update"),
    path('horse/<int:pk>/delete/',
         views.HorseDelete.as_view(), name="horse-delete"),
    # Download
    path('horsedownload/', views.horse_download,
         name="horse-download"),
    path('horsemetadownload/', views.horse_meta_download,
         name="horse-metadownload"),
]
        

urlpatterns += [
    path('camel/create/', views.CamelCreate.as_view(),
         name="camel-create"),

    path('camels/', views.CamelListView.as_view(), name='camels'),
    path('camels_all/', views.CamelListViewAll.as_view(), name='camels_all'),
    path('camel/<int:pk>', views.CamelDetailView.as_view(),
         name='camel-detail'),
    path('camel/<int:pk>/update/',
         views.CamelUpdate.as_view(), name="camel-update"),
    path('camel/<int:pk>/delete/',
         views.CamelDelete.as_view(), name="camel-delete"),
    # Download
    path('cameldownload/', views.camel_download,
         name="camel-download"),
    path('camelmetadownload/', views.camel_meta_download,
         name="camel-metadownload"),
]
        

urlpatterns += [
    path('elephant/create/', views.ElephantCreate.as_view(),
         name="elephant-create"),

    path('elephants/', views.ElephantListView.as_view(), name='elephants'),
    path('elephants_all/', views.ElephantListViewAll.as_view(), name='elephants_all'),
    path('elephant/<int:pk>', views.ElephantDetailView.as_view(),
         name='elephant-detail'),
    path('elephant/<int:pk>/update/',
         views.ElephantUpdate.as_view(), name="elephant-update"),
    path('elephant/<int:pk>/delete/',
         views.ElephantDelete.as_view(), name="elephant-delete"),
    # Download
    path('elephantdownload/', views.elephant_download,
         name="elephant-download"),
    path('elephantmetadownload/', views.elephant_meta_download,
         name="elephant-metadownload"),
]
        

urlpatterns += [
    path('wood_bark_etc/create/', views.Wood_bark_etcCreate.as_view(),
         name="wood_bark_etc-create"),

    path('wood_bark_etcs/', views.Wood_bark_etcListView.as_view(), name='wood_bark_etcs'),
    path('wood_bark_etcs_all/', views.Wood_bark_etcListViewAll.as_view(), name='wood_bark_etcs_all'),
    path('wood_bark_etc/<int:pk>', views.Wood_bark_etcDetailView.as_view(),
         name='wood_bark_etc-detail'),
    path('wood_bark_etc/<int:pk>/update/',
         views.Wood_bark_etcUpdate.as_view(), name="wood_bark_etc-update"),
    path('wood_bark_etc/<int:pk>/delete/',
         views.Wood_bark_etcDelete.as_view(), name="wood_bark_etc-delete"),
    # Download
    path('wood_bark_etcdownload/', views.wood_bark_etc_download,
         name="wood_bark_etc-download"),
    path('wood_bark_etcmetadownload/', views.wood_bark_etc_meta_download,
         name="wood_bark_etc-metadownload"),
]
        

urlpatterns += [
    path('leather_cloth/create/', views.Leather_clothCreate.as_view(),
         name="leather_cloth-create"),

    path('leather_cloths/', views.Leather_clothListView.as_view(), name='leather_cloths'),
    path('leather_cloths_all/', views.Leather_clothListViewAll.as_view(), name='leather_cloths_all'),
    path('leather_cloth/<int:pk>', views.Leather_clothDetailView.as_view(),
         name='leather_cloth-detail'),
    path('leather_cloth/<int:pk>/update/',
         views.Leather_clothUpdate.as_view(), name="leather_cloth-update"),
    path('leather_cloth/<int:pk>/delete/',
         views.Leather_clothDelete.as_view(), name="leather_cloth-delete"),
    # Download
    path('leather_clothdownload/', views.leather_cloth_download,
         name="leather_cloth-download"),
    path('leather_clothmetadownload/', views.leather_cloth_meta_download,
         name="leather_cloth-metadownload"),
]
        

urlpatterns += [
    path('shield/create/', views.ShieldCreate.as_view(),
         name="shield-create"),

    path('shields/', views.ShieldListView.as_view(), name='shields'),
    path('shields_all/', views.ShieldListViewAll.as_view(), name='shields_all'),
    path('shield/<int:pk>', views.ShieldDetailView.as_view(),
         name='shield-detail'),
    path('shield/<int:pk>/update/',
         views.ShieldUpdate.as_view(), name="shield-update"),
    path('shield/<int:pk>/delete/',
         views.ShieldDelete.as_view(), name="shield-delete"),
    # Download
    path('shielddownload/', views.shield_download,
         name="shield-download"),
    path('shieldmetadownload/', views.shield_meta_download,
         name="shield-metadownload"),
]
        

urlpatterns += [
    path('helmet/create/', views.HelmetCreate.as_view(),
         name="helmet-create"),

    path('helmets/', views.HelmetListView.as_view(), name='helmets'),
    path('helmets_all/', views.HelmetListViewAll.as_view(), name='helmets_all'),
    path('helmet/<int:pk>', views.HelmetDetailView.as_view(),
         name='helmet-detail'),
    path('helmet/<int:pk>/update/',
         views.HelmetUpdate.as_view(), name="helmet-update"),
    path('helmet/<int:pk>/delete/',
         views.HelmetDelete.as_view(), name="helmet-delete"),
    # Download
    path('helmetdownload/', views.helmet_download,
         name="helmet-download"),
    path('helmetmetadownload/', views.helmet_meta_download,
         name="helmet-metadownload"),
]
        

urlpatterns += [
    path('breastplate/create/', views.BreastplateCreate.as_view(),
         name="breastplate-create"),

    path('breastplates/', views.BreastplateListView.as_view(), name='breastplates'),
    path('breastplates_all/', views.BreastplateListViewAll.as_view(), name='breastplates_all'),
    path('breastplate/<int:pk>', views.BreastplateDetailView.as_view(),
         name='breastplate-detail'),
    path('breastplate/<int:pk>/update/',
         views.BreastplateUpdate.as_view(), name="breastplate-update"),
    path('breastplate/<int:pk>/delete/',
         views.BreastplateDelete.as_view(), name="breastplate-delete"),
    # Download
    path('breastplatedownload/', views.breastplate_download,
         name="breastplate-download"),
    path('breastplatemetadownload/', views.breastplate_meta_download,
         name="breastplate-metadownload"),
]
        

urlpatterns += [
    path('limb_protection/create/', views.Limb_protectionCreate.as_view(),
         name="limb_protection-create"),

    path('limb_protections/', views.Limb_protectionListView.as_view(), name='limb_protections'),
    path('limb_protections_all/', views.Limb_protectionListViewAll.as_view(), name='limb_protections_all'),
    path('limb_protection/<int:pk>', views.Limb_protectionDetailView.as_view(),
         name='limb_protection-detail'),
    path('limb_protection/<int:pk>/update/',
         views.Limb_protectionUpdate.as_view(), name="limb_protection-update"),
    path('limb_protection/<int:pk>/delete/',
         views.Limb_protectionDelete.as_view(), name="limb_protection-delete"),
    # Download
    path('limb_protectiondownload/', views.limb_protection_download,
         name="limb_protection-download"),
    path('limb_protectionmetadownload/', views.limb_protection_meta_download,
         name="limb_protection-metadownload"),
]
        

urlpatterns += [
    path('scaled_armor/create/', views.Scaled_armorCreate.as_view(),
         name="scaled_armor-create"),

    path('scaled_armors/', views.Scaled_armorListView.as_view(), name='scaled_armors'),
    path('scaled_armors_all/', views.Scaled_armorListViewAll.as_view(), name='scaled_armors_all'),
    path('scaled_armor/<int:pk>', views.Scaled_armorDetailView.as_view(),
         name='scaled_armor-detail'),
    path('scaled_armor/<int:pk>/update/',
         views.Scaled_armorUpdate.as_view(), name="scaled_armor-update"),
    path('scaled_armor/<int:pk>/delete/',
         views.Scaled_armorDelete.as_view(), name="scaled_armor-delete"),
    # Download
    path('scaled_armordownload/', views.scaled_armor_download,
         name="scaled_armor-download"),
    path('scaled_armormetadownload/', views.scaled_armor_meta_download,
         name="scaled_armor-metadownload"),
]
        

urlpatterns += [
    path('laminar_armor/create/', views.Laminar_armorCreate.as_view(),
         name="laminar_armor-create"),

    path('laminar_armors/', views.Laminar_armorListView.as_view(), name='laminar_armors'),
    path('laminar_armors_all/', views.Laminar_armorListViewAll.as_view(), name='laminar_armors_all'),
    path('laminar_armor/<int:pk>', views.Laminar_armorDetailView.as_view(),
         name='laminar_armor-detail'),
    path('laminar_armor/<int:pk>/update/',
         views.Laminar_armorUpdate.as_view(), name="laminar_armor-update"),
    path('laminar_armor/<int:pk>/delete/',
         views.Laminar_armorDelete.as_view(), name="laminar_armor-delete"),
    # Download
    path('laminar_armordownload/', views.laminar_armor_download,
         name="laminar_armor-download"),
    path('laminar_armormetadownload/', views.laminar_armor_meta_download,
         name="laminar_armor-metadownload"),
]
        

urlpatterns += [
    path('plate_armor/create/', views.Plate_armorCreate.as_view(),
         name="plate_armor-create"),

    path('plate_armors/', views.Plate_armorListView.as_view(), name='plate_armors'),
    path('plate_armors_all/', views.Plate_armorListViewAll.as_view(), name='plate_armors_all'),
    path('plate_armor/<int:pk>', views.Plate_armorDetailView.as_view(),
         name='plate_armor-detail'),
    path('plate_armor/<int:pk>/update/',
         views.Plate_armorUpdate.as_view(), name="plate_armor-update"),
    path('plate_armor/<int:pk>/delete/',
         views.Plate_armorDelete.as_view(), name="plate_armor-delete"),
    # Download
    path('plate_armordownload/', views.plate_armor_download,
         name="plate_armor-download"),
    path('plate_armormetadownload/', views.plate_armor_meta_download,
         name="plate_armor-metadownload"),
]
        

urlpatterns += [
    path('small_vessels_canoes_etc/create/', views.Small_vessels_canoes_etcCreate.as_view(),
         name="small_vessels_canoes_etc-create"),

    path('small_vessels_canoes_etcs/', views.Small_vessels_canoes_etcListView.as_view(), name='small_vessels_canoes_etcs'),
    path('small_vessels_canoes_etcs_all/', views.Small_vessels_canoes_etcListViewAll.as_view(), name='small_vessels_canoes_etcs_all'),
    path('small_vessels_canoes_etc/<int:pk>', views.Small_vessels_canoes_etcDetailView.as_view(),
         name='small_vessels_canoes_etc-detail'),
    path('small_vessels_canoes_etc/<int:pk>/update/',
         views.Small_vessels_canoes_etcUpdate.as_view(), name="small_vessels_canoes_etc-update"),
    path('small_vessels_canoes_etc/<int:pk>/delete/',
         views.Small_vessels_canoes_etcDelete.as_view(), name="small_vessels_canoes_etc-delete"),
    # Download
    path('small_vessels_canoes_etcdownload/', views.small_vessels_canoes_etc_download,
         name="small_vessels_canoes_etc-download"),
    path('small_vessels_canoes_etcmetadownload/', views.small_vessels_canoes_etc_meta_download,
         name="small_vessels_canoes_etc-metadownload"),
]
        

urlpatterns += [
    path('merchant_ships_pressed_into_service/create/', views.Merchant_ships_pressed_into_serviceCreate.as_view(),
         name="merchant_ships_pressed_into_service-create"),

    path('merchant_ships_pressed_into_services/', views.Merchant_ships_pressed_into_serviceListView.as_view(), name='merchant_ships_pressed_into_services'),
    path('merchant_ships_pressed_into_services_all/', views.Merchant_ships_pressed_into_serviceListViewAll.as_view(), name='merchant_ships_pressed_into_services_all'),
    path('merchant_ships_pressed_into_service/<int:pk>', views.Merchant_ships_pressed_into_serviceDetailView.as_view(),
         name='merchant_ships_pressed_into_service-detail'),
    path('merchant_ships_pressed_into_service/<int:pk>/update/',
         views.Merchant_ships_pressed_into_serviceUpdate.as_view(), name="merchant_ships_pressed_into_service-update"),
    path('merchant_ships_pressed_into_service/<int:pk>/delete/',
         views.Merchant_ships_pressed_into_serviceDelete.as_view(), name="merchant_ships_pressed_into_service-delete"),
    # Download
    path('merchant_ships_pressed_into_servicedownload/', views.merchant_ships_pressed_into_service_download,
         name="merchant_ships_pressed_into_service-download"),
    path('merchant_ships_pressed_into_servicemetadownload/', views.merchant_ships_pressed_into_service_meta_download,
         name="merchant_ships_pressed_into_service-metadownload"),
]
        

urlpatterns += [
    path('specialized_military_vessel/create/', views.Specialized_military_vesselCreate.as_view(),
         name="specialized_military_vessel-create"),

    path('specialized_military_vessels/', views.Specialized_military_vesselListView.as_view(), name='specialized_military_vessels'),
    path('specialized_military_vessels_all/', views.Specialized_military_vesselListViewAll.as_view(), name='specialized_military_vessels_all'),
    path('specialized_military_vessel/<int:pk>', views.Specialized_military_vesselDetailView.as_view(),
         name='specialized_military_vessel-detail'),
    path('specialized_military_vessel/<int:pk>/update/',
         views.Specialized_military_vesselUpdate.as_view(), name="specialized_military_vessel-update"),
    path('specialized_military_vessel/<int:pk>/delete/',
         views.Specialized_military_vesselDelete.as_view(), name="specialized_military_vessel-delete"),
    # Download
    path('specialized_military_vesseldownload/', views.specialized_military_vessel_download,
         name="specialized_military_vessel-download"),
    path('specialized_military_vesselmetadownload/', views.specialized_military_vessel_meta_download,
         name="specialized_military_vessel-metadownload"),
]
        

urlpatterns += [
    path('settlements_in_a_defensive_position/create/', views.Settlements_in_a_defensive_positionCreate.as_view(),
         name="settlements_in_a_defensive_position-create"),

    path('settlements_in_a_defensive_positions/', views.Settlements_in_a_defensive_positionListView.as_view(), name='settlements_in_a_defensive_positions'),
    path('settlements_in_a_defensive_positions_all/', views.Settlements_in_a_defensive_positionListViewAll.as_view(), name='settlements_in_a_defensive_positions_all'),
    path('settlements_in_a_defensive_position/<int:pk>', views.Settlements_in_a_defensive_positionDetailView.as_view(),
         name='settlements_in_a_defensive_position-detail'),
    path('settlements_in_a_defensive_position/<int:pk>/update/',
         views.Settlements_in_a_defensive_positionUpdate.as_view(), name="settlements_in_a_defensive_position-update"),
    path('settlements_in_a_defensive_position/<int:pk>/delete/',
         views.Settlements_in_a_defensive_positionDelete.as_view(), name="settlements_in_a_defensive_position-delete"),
    # Download
    path('settlements_in_a_defensive_positiondownload/', views.settlements_in_a_defensive_position_download,
         name="settlements_in_a_defensive_position-download"),
    path('settlements_in_a_defensive_positionmetadownload/', views.settlements_in_a_defensive_position_meta_download,
         name="settlements_in_a_defensive_position-metadownload"),
]
        

urlpatterns += [
    path('wooden_palisade/create/', views.Wooden_palisadeCreate.as_view(),
         name="wooden_palisade-create"),

    path('wooden_palisades/', views.Wooden_palisadeListView.as_view(), name='wooden_palisades'),
    path('wooden_palisades_all/', views.Wooden_palisadeListViewAll.as_view(), name='wooden_palisades_all'),
    path('wooden_palisade/<int:pk>', views.Wooden_palisadeDetailView.as_view(),
         name='wooden_palisade-detail'),
    path('wooden_palisade/<int:pk>/update/',
         views.Wooden_palisadeUpdate.as_view(), name="wooden_palisade-update"),
    path('wooden_palisade/<int:pk>/delete/',
         views.Wooden_palisadeDelete.as_view(), name="wooden_palisade-delete"),
    # Download
    path('wooden_palisadedownload/', views.wooden_palisade_download,
         name="wooden_palisade-download"),
    path('wooden_palisademetadownload/', views.wooden_palisade_meta_download,
         name="wooden_palisade-metadownload"),
]
        

urlpatterns += [
    path('earth_rampart/create/', views.Earth_rampartCreate.as_view(),
         name="earth_rampart-create"),

    path('earth_ramparts/', views.Earth_rampartListView.as_view(), name='earth_ramparts'),
    path('earth_ramparts_all/', views.Earth_rampartListViewAll.as_view(), name='earth_ramparts_all'),
    path('earth_rampart/<int:pk>', views.Earth_rampartDetailView.as_view(),
         name='earth_rampart-detail'),
    path('earth_rampart/<int:pk>/update/',
         views.Earth_rampartUpdate.as_view(), name="earth_rampart-update"),
    path('earth_rampart/<int:pk>/delete/',
         views.Earth_rampartDelete.as_view(), name="earth_rampart-delete"),
    # Download
    path('earth_rampartdownload/', views.earth_rampart_download,
         name="earth_rampart-download"),
    path('earth_rampartmetadownload/', views.earth_rampart_meta_download,
         name="earth_rampart-metadownload"),
]
        

urlpatterns += [
    path('ditch/create/', views.DitchCreate.as_view(),
         name="ditch-create"),

    path('ditchs/', views.DitchListView.as_view(), name='ditchs'),
    path('ditchs_all/', views.DitchListViewAll.as_view(), name='ditchs_all'),
    path('ditch/<int:pk>', views.DitchDetailView.as_view(),
         name='ditch-detail'),
    path('ditch/<int:pk>/update/',
         views.DitchUpdate.as_view(), name="ditch-update"),
    path('ditch/<int:pk>/delete/',
         views.DitchDelete.as_view(), name="ditch-delete"),
    # Download
    path('ditchdownload/', views.ditch_download,
         name="ditch-download"),
    path('ditchmetadownload/', views.ditch_meta_download,
         name="ditch-metadownload"),
]
        

urlpatterns += [
    path('moat/create/', views.MoatCreate.as_view(),
         name="moat-create"),

    path('moats/', views.MoatListView.as_view(), name='moats'),
    path('moats_all/', views.MoatListViewAll.as_view(), name='moats_all'),
    path('moat/<int:pk>', views.MoatDetailView.as_view(),
         name='moat-detail'),
    path('moat/<int:pk>/update/',
         views.MoatUpdate.as_view(), name="moat-update"),
    path('moat/<int:pk>/delete/',
         views.MoatDelete.as_view(), name="moat-delete"),
    # Download
    path('moatdownload/', views.moat_download,
         name="moat-download"),
    path('moatmetadownload/', views.moat_meta_download,
         name="moat-metadownload"),
]
        

urlpatterns += [
    path('stone_walls_non_mortared/create/', views.Stone_walls_non_mortaredCreate.as_view(),
         name="stone_walls_non_mortared-create"),

    path('stone_walls_non_mortareds/', views.Stone_walls_non_mortaredListView.as_view(), name='stone_walls_non_mortareds'),
    path('stone_walls_non_mortareds_all/', views.Stone_walls_non_mortaredListViewAll.as_view(), name='stone_walls_non_mortareds_all'),
    path('stone_walls_non_mortared/<int:pk>', views.Stone_walls_non_mortaredDetailView.as_view(),
         name='stone_walls_non_mortared-detail'),
    path('stone_walls_non_mortared/<int:pk>/update/',
         views.Stone_walls_non_mortaredUpdate.as_view(), name="stone_walls_non_mortared-update"),
    path('stone_walls_non_mortared/<int:pk>/delete/',
         views.Stone_walls_non_mortaredDelete.as_view(), name="stone_walls_non_mortared-delete"),
    # Download
    path('stone_walls_non_mortareddownload/', views.stone_walls_non_mortared_download,
         name="stone_walls_non_mortared-download"),
    path('stone_walls_non_mortaredmetadownload/', views.stone_walls_non_mortared_meta_download,
         name="stone_walls_non_mortared-metadownload"),
]
        

urlpatterns += [
    path('stone_walls_mortared/create/', views.Stone_walls_mortaredCreate.as_view(),
         name="stone_walls_mortared-create"),

    path('stone_walls_mortareds/', views.Stone_walls_mortaredListView.as_view(), name='stone_walls_mortareds'),
    path('stone_walls_mortareds_all/', views.Stone_walls_mortaredListViewAll.as_view(), name='stone_walls_mortareds_all'),
    path('stone_walls_mortared/<int:pk>', views.Stone_walls_mortaredDetailView.as_view(),
         name='stone_walls_mortared-detail'),
    path('stone_walls_mortared/<int:pk>/update/',
         views.Stone_walls_mortaredUpdate.as_view(), name="stone_walls_mortared-update"),
    path('stone_walls_mortared/<int:pk>/delete/',
         views.Stone_walls_mortaredDelete.as_view(), name="stone_walls_mortared-delete"),
    # Download
    path('stone_walls_mortareddownload/', views.stone_walls_mortared_download,
         name="stone_walls_mortared-download"),
    path('stone_walls_mortaredmetadownload/', views.stone_walls_mortared_meta_download,
         name="stone_walls_mortared-metadownload"),
]
        

urlpatterns += [
    path('fortified_camp/create/', views.Fortified_campCreate.as_view(),
         name="fortified_camp-create"),

    path('fortified_camps/', views.Fortified_campListView.as_view(), name='fortified_camps'),
    path('fortified_camps_all/', views.Fortified_campListViewAll.as_view(), name='fortified_camps_all'),
    path('fortified_camp/<int:pk>', views.Fortified_campDetailView.as_view(),
         name='fortified_camp-detail'),
    path('fortified_camp/<int:pk>/update/',
         views.Fortified_campUpdate.as_view(), name="fortified_camp-update"),
    path('fortified_camp/<int:pk>/delete/',
         views.Fortified_campDelete.as_view(), name="fortified_camp-delete"),
    # Download
    path('fortified_campdownload/', views.fortified_camp_download,
         name="fortified_camp-download"),
    path('fortified_campmetadownload/', views.fortified_camp_meta_download,
         name="fortified_camp-metadownload"),
]
        

urlpatterns += [
    path('complex_fortification/create/', views.Complex_fortificationCreate.as_view(),
         name="complex_fortification-create"),

    path('complex_fortifications/', views.Complex_fortificationListView.as_view(), name='complex_fortifications'),
    path('complex_fortifications_all/', views.Complex_fortificationListViewAll.as_view(), name='complex_fortifications_all'),
    path('complex_fortification/<int:pk>', views.Complex_fortificationDetailView.as_view(),
         name='complex_fortification-detail'),
    path('complex_fortification/<int:pk>/update/',
         views.Complex_fortificationUpdate.as_view(), name="complex_fortification-update"),
    path('complex_fortification/<int:pk>/delete/',
         views.Complex_fortificationDelete.as_view(), name="complex_fortification-delete"),
    # Download
    path('complex_fortificationdownload/', views.complex_fortification_download,
         name="complex_fortification-download"),
    path('complex_fortificationmetadownload/', views.complex_fortification_meta_download,
         name="complex_fortification-metadownload"),
]
        

urlpatterns += [
    path('modern_fortification/create/', views.Modern_fortificationCreate.as_view(),
         name="modern_fortification-create"),

    path('modern_fortifications/', views.Modern_fortificationListView.as_view(), name='modern_fortifications'),
    path('modern_fortifications_all/', views.Modern_fortificationListViewAll.as_view(), name='modern_fortifications_all'),
    path('modern_fortification/<int:pk>', views.Modern_fortificationDetailView.as_view(),
         name='modern_fortification-detail'),
    path('modern_fortification/<int:pk>/update/',
         views.Modern_fortificationUpdate.as_view(), name="modern_fortification-update"),
    path('modern_fortification/<int:pk>/delete/',
         views.Modern_fortificationDelete.as_view(), name="modern_fortification-delete"),
    # Download
    path('modern_fortificationdownload/', views.modern_fortification_download,
         name="modern_fortification-download"),
    path('modern_fortificationmetadownload/', views.modern_fortification_meta_download,
         name="modern_fortification-metadownload"),
]
        

urlpatterns += [
    path('chainmail/create/', views.ChainmailCreate.as_view(),
         name="chainmail-create"),

    path('chainmails/', views.ChainmailListView.as_view(), name='chainmails'),
    path('chainmails_all/', views.ChainmailListViewAll.as_view(), name='chainmails_all'),
    path('chainmail/<int:pk>', views.ChainmailDetailView.as_view(),
         name='chainmail-detail'),
    path('chainmail/<int:pk>/update/',
         views.ChainmailUpdate.as_view(), name="chainmail-update"),
    path('chainmail/<int:pk>/delete/',
         views.ChainmailDelete.as_view(), name="chainmail-delete"),
    # Download
    path('chainmaildownload/', views.chainmail_download,
         name="chainmail-download"),
    path('chainmailmetadownload/', views.chainmail_meta_download,
         name="chainmail-metadownload"),
]
        