from django.db import models

# Create your models here.

class siteSetting(models.Model):
    banner = models.ImageField(upload_to="media/site")
    Caption = models.TextField()