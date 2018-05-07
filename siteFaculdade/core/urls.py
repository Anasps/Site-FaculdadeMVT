from django.contrib import admin
from django.urls import include, path
from siteFaculdade.core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
]
