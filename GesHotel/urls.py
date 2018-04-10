# -*- coding: utf-8 -*-

from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [

    url('^$', views.acceuil, name='accueil'),

]
