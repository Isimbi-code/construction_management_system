from django.db import models
from django.contrib.auth.models import User



class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invetory_items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name

    @property
    def total_value(self):
        return self.quantity * self.unit_price

