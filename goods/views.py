from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from user.models import User
from .models import *


# Create your views here.
def index(request):
    if request.session['user_id']:
        user_id = request.session['user_id']
        user_name = User.objects.get(id=user_id).uname
    typelist = typeInfo.objects.all()
    type00 = typelist[0].goods_set.order_by('-id')[0:4]
    type01 = typelist[0].goods_set.order_by('-gclick')[0:4]
    type10 = typelist[1].goods_set.order_by('-id')[0:4]
    type11 = typelist[1].goods_set.order_by('-gclick')[0:4]
    type20 = typelist[2].goods_set.order_by('-id')[0:4]
    type21 = typelist[2].goods_set.order_by('-gclick')[0:4]
    type30 = typelist[3].goods_set.order_by('-id')[0:4]
    type31 = typelist[3].goods_set.order_by('-gclick')[0:4]
    type40 = typelist[4].goods_set.order_by('-id')[0:4]
    type41 = typelist[4].goods_set.order_by('-gclick')[0:4]
    type50 = typelist[5].goods_set.order_by('-id')[0:4]
    type51 = typelist[5].goods_set.order_by('-gclick')[0:4]
    context = {
        'title': '首页',
        'username':user_name,
        'type00': type00, 'type01': type01,
        'type10': type10, 'type11': type11,
        'type20': type20, 'type21': type21,
        'type30': type30, 'type31': type31,
        'type40': type40, 'type41': type41,
        'type50': type50, 'type51': type51,
    }
    return render(request, 'goods/index.html', context)


def list(request, tid, pindex, sort):
    '''tid,pindex,sort'''
    typelist = typeInfo.objects.get(pk=int(tid))
    print(tid, pindex, sort)
    news = typelist.goods_set.order_by('-id')[0:2]
    if sort == '1':
        goods_list = goods.objects.filter(gtype_id=int(tid)).order_by('-id')
    elif sort == '2':
        goods_list = goods.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort == '3':
        goods_list = goods.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    paginator = Paginator(goods_list, 10)
    page = paginator.page(int(pindex))
    context = {
        'title': typelist.ttitle, 'page': page,
        'paginator': paginator, 'typeinfo': typelist,
        'sort': sort, 'news': news
    }
    return render(request, 'goods/list.html', context)


def detail(request,gid):
    good=goods.objects.filter(id=gid).first()
    context={
        'title':good.gtitle,'g':good,
    }
    return render(request,'goods/detail.html',context)



def search(request):
    title='搜索结果'
    if request.GET.get('search'):
        keywords = request.GET.get('search')
        print(keywords)
        searchresults = goods.objects.filter(Q(gtitle__icontains=keywords)|Q(gdigest__icontains=keywords)|Q(gcontext__icontains=keywords))
        if(searchresults):
            return render(request,'goods/search.html',locals())
        else:
            return render(request, 'goods/search_error.html', locals())
    else:
        searchresults=''
        return render(request, 'goods/search_error.html',locals())
