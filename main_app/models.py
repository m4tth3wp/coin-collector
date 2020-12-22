from django.db import models

# Create your models here.
class Coin(models.Model):
  name = models.CharField(max_length=100)
  currency = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  value = models.IntegerField()

  def __str__(self):
    return self.name