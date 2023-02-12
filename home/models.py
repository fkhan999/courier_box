from django.db import models

class boxes(models.Model):
    status=models.BooleanField(default=0)

class courierRecieved(models.Model):
    mobile_number=models.CharField(max_length=10)
    otp=models.CharField(max_length=6)
    box=models.IntegerField()
    
