from django.contrib import admin
from django.urls import path, include
from siteFaculdade.core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('siteFaculdade.core.urls')),
    path('presencial/', include('siteFaculdade.presencial.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
