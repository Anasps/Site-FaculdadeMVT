from django.contrib import admin
from django.urls import include, path
from siteFaculdade.core.views import IndexView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
