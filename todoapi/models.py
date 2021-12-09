from django.db import models

# Create your models here.
# models.py
from django.db import models
class Todo(models.Model):
    task = models.CharField(max_length=60)
    completed = models.BooleanField(default=False)
    date_added =  models.DateTimeField(auto_now=False)
    date_completed = models.DateTimeField(auto_now=False)
    def __str__(self):
        return self.name