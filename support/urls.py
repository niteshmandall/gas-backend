from django.urls import path
from . import views

urlpatterns = [
    path('manage/', views.manage_requests, name='manage_requests'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),
    path('request/<int:request_id>/update/', views.update_request_status, name='update_request_status'),
    path('test/', views.test, name='test'),
]
