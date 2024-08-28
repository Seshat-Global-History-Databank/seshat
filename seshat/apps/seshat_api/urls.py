from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r"politys-api", views.PolityViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += [
    path("refs/", views.reference_list),
    path("refs/<int:pk>/", views.reference_detail),
    path("albums/", views.album_list),
    path("albums/<int:pk>/", views.album_detail),
]
