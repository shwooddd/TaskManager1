import datetime

from django.db import models
from django.utils import timezone



class Task(models.Model)
    Task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Base(models.Model):
    Base_text = models.CharField(max_length=500)

class Status(models.Model):
    Status_choice = (
        ('PENDING', 'pending'),
        ('DONE', 'done')
    )
