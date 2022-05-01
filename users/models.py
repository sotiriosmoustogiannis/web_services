from pickle import TRUE
from django.db import models
#from fields import PickledObjectField
from django.contrib.auth.models import User
from pytz import timezone
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'


class Shop(models.Model):
    store_name = models.CharField(max_length=100)
    date_loaded = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.store_name

    def get_absolute_url(self):
       return reverse('shop')

class Pickles(models.Model):
    store_pickle_before = models.FileField(null=True)
    store_pickle_after = models.FileField(null=True)
    #shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def _str__(self):
        return self.pk