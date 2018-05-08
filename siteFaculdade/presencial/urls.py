from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from siteFaculdade.presencial.views import IndexView

app_name = 'presencial'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)