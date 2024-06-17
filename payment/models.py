# models.py

from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_charge_id = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of {self.amount} with charge ID {self.stripe_charge_id}"
