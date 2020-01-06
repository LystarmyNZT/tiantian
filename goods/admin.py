from django.contrib import admin
from .models import *
# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gclick','gdigest','gcontext','gkucun','gtype']
admin.site.register(typeInfo,TypeInfoAdmin)
admin.site.register(goods,GoodsInfoAdmin)