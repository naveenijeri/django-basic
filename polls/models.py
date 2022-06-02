import datetime
from django.db import models
from django.db.models import signals
from django.dispatch import receiver

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=32)

    def __str__(self):
        return self.name

@receiver(signals.pre_save, sender=Customer)
def create_customer(sender,instance,**kwargs):
    print("Pre save is called")

@receiver(signals.post_save, sender=Customer)
def create_customer(sender, instance, created, **kwargs):
    if created:
        print("Post save is called")

@receiver(signals.pre_delete, sender=Customer)
def customer_delete(sender,instance,**kwargs):
    print("Pre delete is called")

@receiver(signals.post_delete, sender=Customer,)
def customer_delete(sender,instance,**kwargs):
    print("Post delete is called")