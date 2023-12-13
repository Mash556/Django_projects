from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    psevdonim = models.CharField(max_length=40)