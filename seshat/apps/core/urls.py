from django.urls import path, re_path

from . import views
from .specific_views import downloads

urlpatterns = [
    path("", views.IndexView.as_view(), name="seshat-index"),
    path("methods/", views.MethodsView.as_view(), name="seshat-methods"),
    path("whoweare/", views.WhoWeAreView.as_view(), name="seshat-whoweare"),
    path("codebook", views.CodebookView.as_view(), name="seshat-codebook"),  # noqa: E501  TODO: The codebook_view is not used anywhere in the codebase
    path("code_book_new_1", views.CodebookNewView.as_view(), name="code_book_1"),
    path("downloads_page/", views.DownloadsView.as_view(), name="seshat-olddownloads"),
    path(
        "acknowledgements/",
        views.AcknowledgementsView.as_view(),
        name="seshat-acknowledgements",
    ),
    path(
        "download_oldcsv/<str:file_name>/",
        downloads.download_oldcsv_view,
        name="download_oldcsv",
    ),
    path(
        "download_csv_all_polities/",
        downloads.download_csv_all_polities_view,
        name="download_csv_all_polities",
    ),
    path(
        "polity_filter_options/",
        views.polity_filter_options_view,
        name="polity_filter_options",
    ),
    path("core/religions_all/", views.ReligionListView.as_view(), name="religion_list"),
    path("core/create_religion/", views.ReligionCreateView.as_view(), name="religion_create"),
    path(
        "core/update_religion/<int:pk>/",
        views.ReligionUpdateView.as_view(),
        name="religion_update",
    ),
    path("core/references/", views.ReferenceListView.as_view(), name="references"),
    path(
        "core/nlp-references/",
        views.NlpReferenceListView.as_view(),
        name="nlp-references",
    ),
    path(
        "core/references/create/",
        views.ReferenceCreateView.as_view(),
        name="reference-create",
    ),
    path(
        "core/references/<int:pk>",
        views.ReferenceDetailView.as_view(),  # noqa: E501  TODO: The reference-detail is not used anywhere in the codebase
        name="reference-detail",
    ),
    path(
        "core/references/<int:pk>/update/",
        views.ReferenceUpdateView.as_view(),
        name="reference-update",
    ),
    path(
        "core/references/<int:pk>/delete/",
        views.ReferenceDeleteView.as_view(),  # noqa: E501  TODO: The no_zotero_refs_list_view is not used anywhere in the codebase
        name="reference-delete",
    ),
    path(
        "core/references/no_zotero_refs_list/",
        views.no_zotero_refs_list_view,  # noqa: E501  TODO: The no_zotero_refs_list_view is not used anywhere in the codebase
        name="no_zotero_refs_list",
    ),
    path(
        "core/references/<int:pk>/updatemodal/",
        views.reference_update_modal_view,  # noqa: E501  TODO: The reference_update_modal_view is not used anywhere in the codebase
        name="reference_update_modal",
    ),
    path(
        "referencesdownload/",
        downloads.referencesdownload_view,  # noqa: E501  TODO: The references_download_view is not used anywhere in the codebase
        name="references_download_view",
    ),
    path(
        "core/polities/create/", views.PolityCreateView.as_view(), name="polity-create"
    ),
    path("core/polities/", views.PolityListView.as_view(), name="polities"),
    path(
        "core/polities-light/",
        views.PolityLightListView.as_view(),
        name="polities-light",
    ),
    path(
        "core/polities_commented/",
        views.PolityCommentedListView.as_view(),
        name="polities-commented",
    ),
    path(
        "core/polity/<int:pk>",
        views.PolityDetailView.as_view(),
        name="polity-detail-main",
    ),
    re_path(
        r"^core/polity/(?P<new_name>[\w-]+)/$",
        views.PolityDetailView.as_view(),  # noqa: E501  TODO: The polity-detail-new-name is not used anywhere in the codebase
        name="polity-detail-new-name",
    ),
    path(
        "core/polities/<int:pk>/update/",
        views.PolityUpdateView.as_view(),
        name="polity-update",
    ),
    path("core/ngas/create/", views.NgaCreateView.as_view(), name="nga-create"),
    path("core/ngas/", views.NgaListView.as_view(), name="ngas"),
    path("core/nga/<int:pk>", views.NgaDetailView.as_view(), name="nga-detail"),
    path(
        "core/ngas/<int:pk>/update/", views.NgaUpdateView.as_view(), name="nga-update"
    ),
    path(
        "core/capitals/create/",
        views.CapitalCreateView.as_view(),
        name="capital-create",
    ),
    path("core/capitals/", views.CapitalListView.as_view(), name="capitals"),
    path(
        "core/capitals/<int:pk>/update/",
        views.CapitalUpdateView.as_view(),
        name="capital-update",
    ),
    path(
        "core/capitals/<int:pk>/delete/",
        views.CapitalDeleteView.as_view(),
        name="capital-delete",
    ),
    path("capitaldownload/", downloads.capital_download_view, name="capital-download"),
    path("search/", views.search_view, name="search"),
    path(
        "search_suggestions/", views.search_suggestions_view, name="search_suggestions"  # noqa: E501  TODO: The search_suggestions_view is not used anywhere in the codebase
    ),
    path("signup/", views.signup_traditional_view, name="signup"),
    path("signup_followup/", views.signupfollowup_view, name="signup-followup"),  # noqa: E501  TODO: The signupfollowup_view is not used anywhere in the codebase
    path(
        "account_activation_sent/",
        views.account_activation_sent_view,
        name="account_activation_sent",
    ),
    path("activate/<slug:uidb64>/<slug:token>/", views.activate_view, name="activate"),
    path(
        "variablehierarchy/",
        views.variablehierarchy_view,
        name="variablehierarchysetting",
    ),
    path("synczotero/", views.synczotero_view, name="synczotero"),
    path(
        "synczoteromanually/", views.synczoteromanually_view, name="synczoteromanually"
    ),
    path("synczotero100/", views.synczotero100_view, name="synczotero100"),
    path("updatecitations/", views.update_citations_view, name="updatecitations"),
    path(
        "core/citations/create/",
        views.CitationCreateView.as_view(),
        name="citation-create",
    ),
    path("core/citations/", views.CitationListView.as_view(), name="citations"),
    path(
        "core/citations/<slug:id>",
        views.CitationDetailView.as_view(),
        name="citation-detail",
    ),
    path(
        "core/citations/<slug:pk>/update/",
        views.CitationUpdateView.as_view(),
        name="citation-update",
    ),
    path(
        "core/citations/<int:pk>/delete/",
        views.CitationDeleteView.as_view(),
        name="citation-delete",
    ),
    path(
        "core/seshatcomments/create/",
        views.SeshatCommentCreateView.as_view(),
        name="seshatcomment-create",
    ),
    path(
        "core/seshatcomments/",
        views.SeshatCommentListView.as_view(),
        name="seshatcomments",
    ),
    path(
        "core/seshatcomments/<slug:id>",
        views.SeshatCommentDetailView.as_view(),
        name="seshatcomment-detail",
    ),
    path(
        "core/seshatcomments/<int:pk>/update/",
        views.SeshatCommentUpdateView.as_view(),
        name="seshatcomment-update",
    ),
    path(
        "core/seshatcomments/<int:pk>/delete/",
        views.SeshatCommentDeleteView.as_view(),
        name="seshatcomment-delete",
    ),
    path(
        "core/seshatcommentparts/create/",
        views.SeshatCommentPartCreateView.as_view(),
        name="seshatcommentpart-create",
    ),
    path(
        "core/seshatcommentparts/create2/<int:com_id>/<int:subcom_order>/",
        views.seshatcommentparts_create2_view,
        name="seshatcommentpart-create2",
    ),
    path(
        "core/seshatcommentparts/create2_inline/<slug:app_name>/<slug:model_name>/<int:instance_id>/",  # noqa: E501
        views.seshatcommentparts_create2_inline_view,
        name="seshatcommentpart-create2-inline",
    ),
    path(
        "core/seshatcommentparts/",
        views.SeshatCommentPartListView.as_view(),
        name="seshatcommentparts",
    ),
    path(
        "core/seshatcommentparts3/",
        views.SeshatCommentPartListView3.as_view(),
        name="seshatcommentparts3",
    ),
    path(
        "core/seshatcommentparts/<slug:id>",
        views.SeshatCommentPartDetailView.as_view(),
        name="seshatcommentpart-detail",
    ),
    path(
        "core/seshatcommentparts/<int:pk>/update/",
        views.SeshatCommentPartUpdateView.as_view(),
        name="seshatcommentpart-update",
    ),
    path(
        "core/seshatcommentparts/<int:pk>/update2/",
        views.update_seshat_comment_part_view,
        name="seshatcommentpart-update2",
    ),
    path(
        "core/seshatcommentparts/<int:pk>/delete/",
        views.SeshatCommentPartDeleteView.as_view(),
        name="seshatcommentpart-delete",
    ),
    path(
        "core/seshatcommentparts/create3/",
        views.seshatcommentparts_create3_view,
        name="seshatcommentpart_create3",
    ),
    path(
        "core/seshatcomments/create3/",
        views.seshatcomments_create3_view,
        name="seshatcomment_create_view",
    ),
    path(
        "create_subcomment_new/<slug:app_name>/<slug:model_name>/<int:instance_id>/",
        views.create_subcomment_new_view,
        name="create_subcomment_new",
    ),
    path(
        "create_subcomment_newer/<slug:app_name>/<slug:model_name>/<int:instance_id>/",
        views.create_subcomment_newer_view,
        name="create_subcomment_newer",
    ),
    path(
        "create_private_subcomment_new/<slug:app_name>/<slug:model_name>/<int:instance_id>/",  # noqa: E501
        views.create_private_subcomment_new_view,
        name="create_private_subcomment_new",
    ),
    path(
        "core/seshatprivatecomments/<int:pk>/update/",
        views.SeshatPrivateCommentUpdateView.as_view(),
        name="seshatprivatecomment-update",
    ),
    path(
        "core/seshatprivatecommentparts/create2/<int:private_com_id>/",
        views.seshatprivatecommentparts_create2_view,
        name="seshatprivatecommentpart-create2",
    ),
    path(
        "core/seshatprivatecommentparts/<int:pk>/update/<int:private_com_id>/",
        views.SeshatPrivateCommentPartUpdateView.as_view(),
        name="seshatprivatecommentpart-update",
    ),
    path("core/discussion_room/", views.discussion_room_view, name="discussion_room"),
    path("core/nlp_datapoints/", views.nlp_datapoints_view, name="nlp_datapoints"),
    path(
        "core/nlp_datapoints_2/", views.nlp_datapoints_2_view, name="nlp_datapoints_2"
    ),
    # TODO: Correct? The below is commented out as it is not used in the codebase
    # path("core/not_found_404", views.NotFoundView.as_view(), name="four-o-four"),
    path("core/world_map/", views.world_map_view, name="world_map"),
    path(
        "core/world_map_one_year/",
        views.world_map_one_year_view,
        name="world_map_one_year",
    ),
    path("core/world_map_all/", views.world_map_all_view, name="world_map_all"),
    path(
        "core/provinces_and_countries",
        views.provinces_and_countries_view,
        name="provinces_and_countries",
    ),
]
