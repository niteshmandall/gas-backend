from django.db import models
from django.contrib.auth.models import User  # Import User model for the created_by field


class ServiceRequest(models.Model):
    """
    Model for service requests.
    """
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class RequestComment(models.Model):
    """
    Model for comments on service requests.
    """
    service_request = models.ForeignKey(ServiceRequest, related_name='comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.created_by} on {self.service_request}'
