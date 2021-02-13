from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import calendar
# Create your models here.
MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1,13)]

class Medical(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    alergies = models.CharField(max_length=100)

class Pills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pills =  models.CharField(max_length=100)
    exist = models.BooleanField(default=True)
    count = models.IntegerField(default=0)

class Schedule(models.Model):
    pill = models.ForeignKey(Pills, on_delete=models.CASCADE)
    schedule = models.DateTimeField(auto_now_add=False)

class Plans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100, default = "")
    date = models.DateTimeField(default = timezone.now)
