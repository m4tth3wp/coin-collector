from django.forms import ModelForm
from .models import Acquired

class AcquiredForm(ModelForm):
  class Meta:
    model = Acquired
    fields = ['owned', 'date']