from django.urls import path, re_path

from . import views

urlpatterns = [path('', views.seshatindex, name='seshat-index'),]
urlpatterns += [path('methods/', views.seshatmethods, name='seshat-methods'),]
urlpatterns += [path('whoweare/', views.seshatwhoweare, name='seshat-whoweare'),]
urlpatterns += [path('codebook', views.seshatcodebookold, name='seshat-codebook'),]
urlpatterns += [path('downloads_page/', views.seshatolddownloads, name='seshat-olddownloads'),]
urlpatterns += [path('acknowledgements/', views.seshatacknowledgements, name='seshat-acknowledgements'),]
urlpatterns += [path('download_oldcsv/<str:file_name>/', views.download_oldcsv, name='download_oldcsv'),]

urlpatterns += [path('code_book_new_1', views.seshatcodebooknew1, name='code_book_1'),]
#urlpatterns += [path('code_book_new_2', views.download_oldcsv, name='code_book_2'),]

#urlpatterns += [path('home_cards/', views.home_cards, name='home_cards'),]

urlpatterns  += [path('download_csv_all_polities/', views.download_csv_all_polities,name='download_csv_all_polities'),]

    


urlpatterns += [path('polity_filter_options/', views.polity_filter_options_view, name='polity_filter_options'),]


urlpatterns += [
     path('core/religions_all/', views.ReligionListView.as_view(), name='religion_list'),
     path('core/create_religion/', views.religion_create, name='religion_create'),
     path('core/update_religion/<int:pk>/', views.religion_update, name='religion_update'),
     path('core/references/', views.ReferenceListView.as_view(), name='references'),
     path('core/nlp-references/', views.NlpReferenceListView.as_view(), name='nlp-references'),
     path('core/references/create/', views.ReferenceCreate.as_view(),
         name="reference-create"),
     path('core/references/<int:pk>', views.ReferenceDetailView.as_view(),name='reference-detail'),
     path('core/references/<int:pk>/update/',views.ReferenceUpdate.as_view(), name="reference-update"),
    path('core/references/<int:pk>/delete/', views.ReferenceDelete.as_view(), name="reference-delete"),
        path('core/references/no_zotero_refs_list/', views.no_zotero_refs_list, name='no_zotero_refs_list'),
     path('core/references/<int:pk>/updatemodal/', views.reference_update_modal, name='reference_update_modal'),
     path('referencesdownload/', views.references_download,
         name="references_download"),

    path('core/polities/create/', views.PolityCreate.as_view(),
         name="polity-create"),
    path('core/polities/', views.PolityListView.as_view(), name='polities'),
     path('core/polities-light/', views.PolityListViewLight.as_view(), name='polities-light'),

     path('core/polities_commented/', views.PolityListViewCommented.as_view(), name='polities-commented'),
    path('core/polity/<int:pk>', views.PolityDetailView.as_view(), name='polity-detail-main'),
     re_path(r'^core/polity/(?P<new_name>[\w-]+)/$', views.PolityDetailView.as_view(), name='polity-detail-new-name'),

     path('core/polities/<int:pk>/update/',
         views.PolityUpdate.as_view(), name="polity-update"),


    path('core/ngas/create/', views.NgaCreate.as_view(),
         name="nga-create"),
    path('core/ngas/', views.NgaListView.as_view(), name='ngas'),
    path('core/nga/<int:pk>', views.NgaDetailView.as_view(), name='nga-detail'),
     path('core/ngas/<int:pk>/update/',
         views.NgaUpdate.as_view(), name="nga-update"),

    path('core/capitals/create/', views.CapitalCreate.as_view(),
         name="capital-create"),
    path('core/capitals/', views.CapitalListView.as_view(), name='capitals'),
     path('core/capitals/<int:pk>/update/',
         views.CapitalUpdate.as_view(), name="capital-update"),
    path('core/capitals/<int:pk>/delete/',
         views.CapitalDelete.as_view(), name="capital-delete"),
     path('capitaldownload/', views.capital_download,
         name="capital-download"),


    path('search/', views.search_view, name='search'),
     path('search_suggestions/', views.search_suggestions, name='search_suggestions'),
    path('signup/', views.signup_traditional, name='signup'),
    path('signup_followup/', views.signupfollowup, name='signup-followup'),
    # re_path(r'^account_activation_sent/$', views.account_activation_sent,
    #         name='account_activation_sent'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         views.activate, name='activate'),
    path('account_activation_sent/', views.account_activation_sent,
         name='account_activation_sent'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.activate, name='activate'),
    path('variablehierarchy/', views.variablehierarchysetting,
         name='variablehierarchysetting'),
     path('synczotero/', views.synczotero, name='synczotero'),
     path('synczoteromanually/', views.synczoteromanually, name='synczoteromanually'),
     path('synczotero100/', views.synczotero100, name='synczotero100'),
     path('updatecitations/', views.update_citations, name='updatecitations'),
]

urlpatterns += [
    path('core/citations/create/', views.CitationCreate.as_view(),
         name="citation-create"),
     path('core/citations/', views.CitationListView.as_view(), name='citations'),
    path('core/citations/<slug:id>', views.CitationDetailView.as_view(),
         name='citation-detail'),
    path('core/citations/<slug:pk>/update/',
         views.CitationUpdate.as_view(), name="citation-update"),
    path('core/citations/<int:pk>/delete/',
         views.CitationDelete.as_view(), name="citation-delete"),
    # Download
    #path('balancedownload/', views.balance_download,
     #    name="balance-download"),
]

urlpatterns += [
    path('core/seshatcomments/create/', views.SeshatCommentCreate.as_view(),
         name="seshatcomment-create"),
     path('core/seshatcomments/', views.SeshatCommentListView.as_view(), name='seshatcomments'),
    path('core/seshatcomments/<slug:id>', views.SeshatCommentDetailView.as_view(),
         name='seshatcomment-detail'),
    path('core/seshatcomments/<int:pk>/update/',
         views.SeshatCommentUpdate.as_view(), name="seshatcomment-update"),
    path('core/seshatcomments/<int:pk>/delete/',
         views.SeshatCommentDelete.as_view(), name="seshatcomment-delete"),
    # Download
    #path('balancedownload/', views.balance_download,
     #    name="balance-download"),
]

urlpatterns += [
    path('core/seshatcommentparts/create/', views.SeshatCommentPartCreate.as_view(),
         name="seshatcommentpart-create"),
    #path('core/seshatcommentparts/create2/<int:com_id>/<int:subcom_order>/', views.SeshatCommentPartCreate2.as_view(),
    #     name="seshatcommentpart-create2"),
    path('core/seshatcommentparts/create2/<int:com_id>/<int:subcom_order>/', views.seshat_comment_part_create_from_null_view,
         name="seshatcommentpart-create2"),
    path('core/seshatcommentparts/create2_inline/<slug:app_name>/<slug:model_name>/<int:instance_id>/', views.seshat_comment_part_create_from_null_view_inline,
         name="seshatcommentpart-create2-inline"),
     path('core/seshatcommentparts/', views.SeshatCommentPartListView.as_view(), name='seshatcommentparts'),
     path('core/seshatcommentparts3/', views.SeshatCommentPartListView3.as_view(), name='seshatcommentparts3'),
    path('core/seshatcommentparts/<slug:id>', views.SeshatCommentPartDetailView.as_view(),
         name='seshatcommentpart-detail'),
    path('core/seshatcommentparts/<int:pk>/update/',
         views.SeshatCommentPartUpdate.as_view(), name="seshatcommentpart-update"),
    path('core/seshatcommentparts/<int:pk>/update2/',
         views.update_seshat_comment_part_view, name="seshatcommentpart-update2"),
    path('core/seshatcommentparts/<int:pk>/delete/',
         views.SeshatCommentPartDelete.as_view(), name="seshatcommentpart-delete"),
    path('core/seshatcommentparts/create3/', views.seshatcommentpart_create_view, name='seshatcommentpart_create3'),
    path('core/seshatcomments/create3/', views.seshatcomment_create_view, name='seshatcomment_create_view'),

    # NEW
     path('create_subcomment_new/<slug:app_name>/<slug:model_name>/<int:instance_id>/', views.create_a_comment_with_a_subcomment_new, name='create_subcomment_new'),
     path('create_subcomment_newer/<slug:app_name>/<slug:model_name>/<int:instance_id>/', views.create_a_comment_with_a_subcomment_newer, name='create_subcomment_newer'),
     path('create_private_subcomment_new/<slug:app_name>/<slug:model_name>/<int:instance_id>/', views.create_a_private_comment_with_a_private_subcomment_new, name='create_private_subcomment_new'),
     path('core/seshatprivatecomments/<int:pk>/update/',
         views.SeshatPrivateCommentUpdate.as_view(), name="seshatprivatecomment-update"),
     path('core/seshatprivatecommentparts/create2/<int:private_com_id>/', views.seshat_private_comment_part_create_from_null_view,
         name="seshatprivatecommentpart-create2"),

    path('core/seshatprivatecommentparts/<int:pk>/update/<int:private_com_id>/',
         views.SeshatPrivateCommentPartUpdate.as_view(), name="seshatprivatecommentpart-update"),
    path('core/xxyyzz/<int:com_id>/',
         views.xxyyzz, name="xxyyzz"),

    # Download
    #path('balancedownload/', views.balance_download,
     #    name="balance-download"),
]

urlpatterns += [path('core/discussion_room/', views.discussion_room, name="discussion_room"),]
urlpatterns += [path('core/nlp_datapoints/', views.nlp_datapoints, name="nlp_datapoints"),]
urlpatterns += [path('core/nlp_datapoints_2/', views.nlp_datapoints_2, name="nlp_datapoints_2"),]

urlpatterns += [
     path('core/not_found_404', views.four_o_four,
         name="four-o-four"),

]

# Map urls
urlpatterns += [path('core/world_map/', views.map_view_initial, name='world_map'),]
urlpatterns += [path('core/world_map_all/', views.map_view_all, name='world_map_all'),]
urlpatterns += [path('core/world_map_all_with_vars/', views.map_view_all_with_vars, name='world_map_all_with_vars'),]
urlpatterns += [path('core/provinces_and_countries', views.provinces_and_countries_view, name='provinces_and_countries'),]