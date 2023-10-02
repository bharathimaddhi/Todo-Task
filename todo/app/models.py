
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()