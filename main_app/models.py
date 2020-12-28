from django.db import models
from django.urls import reverse

ANSWER = (
  ('Y', 'Yes'),
  ('N', 'No')
)

# Create your models here.
class Coin(models.Model):
  name = models.CharField(max_length=100)
  currency = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  value = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'coin_id': self.id})
  
class Acquired(models.Model):
    owned = models.CharField(
      max_length=100,
      choices=ANSWER,
      default=ANSWER[0][1]
    )
    date = models.DateField()

    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
      return f'{self.get_owned_display()} on {self.date}'
  