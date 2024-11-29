from django.conf.urls.static import static
from django.urls import path

from gas import settings
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_request, name='track_request'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
