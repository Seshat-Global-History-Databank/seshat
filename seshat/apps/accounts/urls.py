from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('userprofile/', views.profile, name='user-profile'),
]

urlpatterns += [
    path('seshat_task/create/', views.Seshat_taskCreate.as_view(),
         name="seshat_task-create"),
    path('seshat_task/<int:pk>', views.Seshat_taskDetailView.as_view(),
         name='seshat_task-detail'),
]

urlpatterns += [
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name="profile-update"),
]
