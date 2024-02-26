from tkinter import CASCADE
from django.db import models
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=255)
    classp = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Gun(models.Model):
    name = models.CharField(max_length=255)
    calibre = models.CharField(max_length=50,  default=1)
    serial_number = models.CharField(max_length=50,  default=1)
    count_ammo = models.IntegerField( default=1)
    
    def __str__(self):
        return self.name


