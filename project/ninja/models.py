from django.db import models

class Clan(models.Model):
    boss=models.CharField(max_length=255)
    count_people=models.IntegerField()
    power=models.IntegerField()
