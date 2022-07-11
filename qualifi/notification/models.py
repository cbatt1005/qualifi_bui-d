from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Notification(models.Model):
    MESSAGE = ''
    APPLICATION = ''
    CHOICES = (
        (MESSAGE, '')
        (APPLICATION, '')
    )
    
    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    