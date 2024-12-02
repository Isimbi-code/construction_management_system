from django.db import models
from django.contrib.auth.models import User
import datetime



class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_employees')  
    POSITION_CHOICES = [
        ('manager', 'Manager'),
        ('laborer', 'Laborer'),
        ('carpenter', 'Carpenter'),
        ('electrician', 'Electrician'),
        ('plumber', 'Plumber'),
        ('mason', 'Mason'),
    ]
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    hire_date = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=100)
    emailAddress = models.CharField(max_length=15)

    

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.PositiveIntegerField(default=10)
    

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dashboard_projects')
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    

