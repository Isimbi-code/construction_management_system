from django.db import models
from django.contrib.auth.models import User
import datetime




class Project(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_projects')
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

