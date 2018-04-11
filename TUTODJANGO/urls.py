"""TUTODJANGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
# from rest_framework import routers
from rest_framework.routers import DefaultRouter

# router = routers.DefaultRouter()

# app_name = 'store'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('GesHotel.urls', 'GesHotel'), namespace="GesHotel")),
    # ajouter le name space au cas ou il a plusieur
    #  applicatons

]
# pour gerer les debug de mon application
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls))
                  ] + urlpatterns
