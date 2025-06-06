from django.db import models

# Create your models here.
class WebhookEvent(models.Model):
    provider = models.CharField(max_length=20, choices=[('paystack', 'Paystack'), ('momo', 'Momo')])
    raw_payload = models.JSONField()
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
