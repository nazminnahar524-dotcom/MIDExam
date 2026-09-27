from django.db import models

# Create your models here.

class Laptop(models.Model):
    brand = models.CharField(max_length=50,blank=False)
    price = models.IntegerField( blank=False)
    imei = models.IntegerField(unique=True)
    color = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.imei)