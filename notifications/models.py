from django.db import models
from users.models import User

# Create your models here.
class NotificationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    method = models.CharField(max_length=20, choices=[('email', 'Email'), ('toast', 'Toast'), ('sms', 'SMS')])
    status = models.CharField(max_length=10, choices=[('sent', 'Sent'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)

