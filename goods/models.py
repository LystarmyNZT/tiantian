from django.db import models

# Create your models here.
class typeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle
    class Meta:
        db_table="goods_typeInfo"
        verbose_name='商品分类'
        verbose_name_plural=verbose_name


class goods(models.Model):
    gtitle=models.CharField(max_length=20)
    gpic=models.ImageField(upload_to='goods')
    gprice=models.DecimalField(max_digits=5,decimal_places=2)
    isDelete=models.BooleanField(default=False)
    gunit=models.CharField(max_length=20,default='500克')
    gclick=models.IntegerField()
    gdigest=models.CharField(max_length=50)
    gcontext=models.CharField(max_length=100)
    gkucun=models.IntegerField()#库存
    gtype=models.ForeignKey(typeInfo,on_delete=1,)#和商品分类对应一对多的关系
    def __str__(self):
        return self.gtitle
    class Meta:
        db_table='goods_goodinfo'
        verbose_name='商品'
        verbose_name_plural=verbose_name

