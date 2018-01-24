from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from geoposition.fields import GeopositionField


class Places(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    # goods = models.ManyToManyField(Goods,related_name='goods')
    position = GeopositionField()

    class Meta:
        verbose_name = 'Places'
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.title

class Goods(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    places = models.ManyToManyField(Places,related_name='places')

    class Meta:
        verbose_name='Goods'
        verbose_name_plural='Goods'

    def __str__(self):
        return self.name
