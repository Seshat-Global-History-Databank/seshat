from django.urls import path

from . import views    



urlpatterns = [
    path('download_csv_settlement_population/', views.settlement_population_download,name='download_csv_settlement_population'),
]