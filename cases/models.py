from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class CaseFile(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('ADJOURNED', 'Adjourned'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='case_files')
    client_name = models.CharField(max_length=255)
    case_number = models.CharField(max_length=100, blank=True, unique=True, null=True)
    court = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    next_hearing_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['client_name']),
            models.Index(fields=['status']),
            models.Index(fields=['next_hearing_date']),
        ]

