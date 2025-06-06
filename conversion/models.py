from django.db import models
from users.models import User


# Create your models here.
class Conversion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_currency = models.CharField(max_length=3, choices=[('NGN', 'Naira'), ('GHS', 'Cedis')])
    to_currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    converted_amount = models.DecimalField(max_digits=12, decimal_places=2)
    fee = models.DecimalField(max_digits=12, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)
