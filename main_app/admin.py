from django.contrib import admin
from .models import Coin, Acquired

# Register your models here.
admin.site.register(Coin)

admin.site.register(Acquired)