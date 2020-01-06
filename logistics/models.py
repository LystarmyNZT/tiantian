from django.db import models

# Create your models here.
class onepath(models.Model):
    order_num=models.CharField(max_length=100)
    startingpoint=models.CharField(max_length=100)
    nowstation=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)


