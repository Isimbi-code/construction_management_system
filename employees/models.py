from django.db import models
import datetime
from django.contrib.auth.models import User




class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees')
    POSITION_CHOICES = [
        ('manager', 'Manager'),
        ('laborer', 'Laborer'),
        ('carpenter', 'Carpenter'),
        ('electrician', 'Electrician'),
        ('plumber', 'Plumber'),
        ('mason', 'Mason'),
    ]
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    hire_date = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.position.title}"

