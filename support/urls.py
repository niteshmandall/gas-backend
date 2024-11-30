from django.urls import path
from . import views

urlpatterns = [
    path('requests/', views.manage_requests, name='manage_requests'),
    path('requests/<int:request_id>/', views.request_detail, name='request_detail'),
    path('requests/<int:request_id>/update/', views.update_request_status, name='update_request_status'),
]
