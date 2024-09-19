from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r"politys-api", views.PolityViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    # Refs
    path("refs/", views.reference_list_view),
    path("refs/<int:pk>/", views.reference_detail_view),
]
