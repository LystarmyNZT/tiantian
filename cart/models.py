from django.db import models

# Create your models here.
#modify by 王紫君
class Cart(models.Model):
    uid=models.CharField(max_length=30)
    gid=models.CharField(max_length=50)
    gcount=models.IntegerField(default=1)