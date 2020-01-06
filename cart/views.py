from django.shortcuts import render

# Create your views here.
# modify by 王紫君
from user.models import User
from cart.models import Cart
from goods.models import goods
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse
def View_user_cart(request):
    user_id = request.session['user_id']
    usergoodslist = Cart.objects.filter(uid=int(user_id))
    res=goods.objects.none()
    for g in usergoodslist:
        good=goods.objects.filter(id=int(g.gid))
        res=res|good

    context={"goodslist":res,}
    return render(request,'cart/cart.html',context)

def Add_user_cart(request):
    user_id=request.session['user_id']

    count=request.GET['count']
    goods_id = request.GET['gid']
    print(goods_id,count)
    cart=Cart.objects.filter(uid=user_id,gid=goods_id).first()
    if cart:
        cart.gcount=cart.gcount+int(count)
    else:
        cart=Cart()
        cart.uid=user_id
        cart.gid=goods_id
        cart.gcount=count
    print(user_id,goods_id,count)
    cart.save()
    return HttpResponse("OK")

def Delete_user_cart(request):
    user_id=request.session['user_id']
    goods_id=request.GET['gid']
    goods_log=Cart.objects.filter(uid=user_id,gid=goods_id).first()
    if goods_log:
        goods_log.delete()

