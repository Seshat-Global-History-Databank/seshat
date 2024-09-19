from django.urls import path, include

from . import views

urlpatterns = [
    path("userprofile/", views.profile_view, name="user-profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "seshat_task/create/",
        views.Seshat_TaskCreateView.as_view(),
        name="seshat_task-create",
    ),
    path(
        "seshat_task/<int:pk>",
        views.Seshat_TaskDetailView.as_view(),
        name="seshat_task-detail",
    ),
    path(
        "profile/<int:pk>/update/",
        views.ProfileUpdateView.as_view(),
        name="profile-update",
    ),
]
