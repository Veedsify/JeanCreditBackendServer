from django.db import models


# Create your models here.
class ExchangeRate(models.Model):
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    source = models.CharField(
        max_length=20, choices=[("api", "API"), ("manual", "Manual")]
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
