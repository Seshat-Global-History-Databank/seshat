"""seshat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#try:
urlpatterns = [
path('admin/', admin.site.urls),
path('', include("seshat.apps.core.urls")),
#path('accounts/', include('django.contrib.auth.urls')),
path('accounts/', include('allauth.urls')),
path('profiles/', include("seshat.apps.accounts.urls")),
path('general/', include('seshat.apps.general.urls')),
path('sc/', include('seshat.apps.sc.urls')),
path('wf/', include('seshat.apps.wf.urls')),
path('rt/', include('seshat.apps.rt.urls')),
path('crisisdb/', include('seshat.apps.crisisdb.urls')),
path('api/', include('seshat.apps.seshat_api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#except:
#    print("ERROR in including one of the url paths above...")
#    urlpatterns=[]

urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls')),
]
