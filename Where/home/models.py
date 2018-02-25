from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from geoposition.fields import GeopositionField
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    des = models.TextField(max_length=200)
    phone = PhoneNumberField()
    position = GeopositionField(null=True)

    def __str__(self):
        return self.title

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

#
# class Places(models.Model):
#     user = models.ForeignKey(User,on_delete = models.CASCADE)
#     title = models.CharField(max_length=200)
#     # goods = models.ManyToManyField(Goods,related_name='goods')
#     position = GeopositionField()
#
#     class Meta:
#         verbose_name = 'Places'
#         verbose_name_plural = 'Places'
#
#     def __str__(self):
#         return self.title

class Goods(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    #places = models.ManyToManyField(Places,related_name='places')
    position = GeopositionField()
    stock = models.IntegerField(default=0)
    out_of = models.IntegerField(default=1)
    created_date = models.DateTimeField(
            default=timezone.now)


    class Meta:
        verbose_name='Goods'
        verbose_name_plural='Goods'

    def __str__(self):
        return self.name
