from django.db import models

# Create your models here.
class User(models.Model):
    uname=models.CharField(max_length=30)
    upwd=models.CharField(max_length=100)
    uemail=models.EmailField()
    ureceiver=models.CharField(max_length=20,default='')
    uaddress=models.CharField(max_length=100,default='')
    uzipcode=models.CharField(max_length=6,default='')
    uphone=models.CharField(max_length=11,default='')