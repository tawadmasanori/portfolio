from django.db import models

# Create your models here.
class PfModel(models.Model):
  title = models.CharField()
  txt = models.TextField()
  
