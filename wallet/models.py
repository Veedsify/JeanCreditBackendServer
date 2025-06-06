from django.db import models
from users.models import User

# Create your models here.
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance_ngn = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    balance_ghs = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)


class Funding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=[('NGN', 'Naira'), ('GHS', 'Cedis')])
    method = models.CharField(max_length=50, choices=[('paystack', 'Paystack'), ('momo', 'Mobile Money')])
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')])
    reference = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
