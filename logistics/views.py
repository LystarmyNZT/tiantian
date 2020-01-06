from django.shortcuts import render

# Create your views here.
from logistics.models import onepath
from user.models import User


def gdmap(request):
    ordernum_a=request.GET.get('ordernum')
    if ordernum_a:
        if onepath.objects.filter(order_num=ordernum_a):
            path = onepath.objects.get(order_num=ordernum_a)
            startpoint = path.startingpoint
            nowstation = path.nowstation
            destination = path.destination
            title='物流跟踪'
            got = True
            return render(request, 'logistics/gdmap.html', locals())
        else:
            got = False
            return render(request, 'logistics/gdmap.html', locals())
    else:
        return render(request, 'logistics/gdmap.html', locals())
