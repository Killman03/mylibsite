from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=150)
