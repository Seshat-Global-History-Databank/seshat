from django.urls import path

from . import views    



urlpatterns = [
    path('download_csv_settlement_population/', views.settlement_population_download,name='download_csv_settlement_population'),
    path('download_csv_settlement_allen_data/', views.generate_stlm_csv_response,name='download_csv_settlement_allen_data'),
]