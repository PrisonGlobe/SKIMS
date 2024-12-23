from django.db import models
from django.contrib.auth.models import User

# These are my tables
# Create your models here.
class HospitalItem(models.Model):
    hospitalName = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hospitalName


class RoomItem(models.Model):
    roomName = models.CharField(max_length=255, null=True)
    floor = models.IntegerField()
    department = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospitalName = models.ForeignKey('HospitalItem', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.roomName


class RackItem(models.Model):
    rackName = models.CharField(max_length=255, null=True)
    binCount = models.IntegerField()
    roomName = models.ForeignKey('RoomItem', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rackName


class BinItem(models.Model):
    binName = models.CharField(max_length=255, null=True)
    binHeight = models.IntegerField()
    binColor = models.CharField(max_length=255, null=True)
    rackName = models.ForeignKey('RackItem', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.binName

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class SupplyItem(models.Model):
    supplyName = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField()
    binName = models.ForeignKey('binItem', on_delete=models.SET_NULL, blank=True, null=True)
    vendor = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255, null=True)
    refNum = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'supplies'

    def __str__(self):
        return self.supplyName







