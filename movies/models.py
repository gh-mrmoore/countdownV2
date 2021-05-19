from django.db import models
import json
from django.http import JsonResponse

# Create your models here.
class MovieCountDown(models.Model):
    # movieOwner (foreign key to user)
    movieId = models.AutoField(primary_key=True, unique=True)
    movieTitle = models.CharField(max_length=250)
    movieDate = models.DateField(blank=False)
    movieSource = models.CharField(max_length=250)