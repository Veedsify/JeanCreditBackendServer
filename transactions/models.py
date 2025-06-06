from django.db import models
from users.models import User


# Create your models here.
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=20,
        choices=[
            ("funding", "Funding"),
            ("conversion", "Conversion"),
            ("withdrawal", "Withdrawal"),
        ],
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=10,
        choices=[("pending", "Pending"), ("success", "Success"), ("failed", "Failed")],
    )
    reference = models.CharField(max_length=100, unique=True)
    direction = models.CharField(
        max_length=20,
        choices=[
            ("NGN-GHS", "Naira to Cedis"),
            ("GHS-NGN", "Cedis to Naira"),
            ("Deposit-Naira", "Deposit To Naira"),
            ("Deposit-Cedis", "Deposit To Cedis"),
        ],
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
