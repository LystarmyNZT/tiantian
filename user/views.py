from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from hashlib import sha1
from user.models import User


def register(request):
    title="用户注册"
    return render(request,'user/register.html',locals())

    # return
def login(request):
    uname=request.COOKIES.get('uname','')
    context = ({
        'title': '用户登录', 'error_name': 0, 'error_pwd': 0,'uname':uname
    })

    title="用户登录"
    return render(request, 'user/login.html', locals())

def register_exist(request):
    uname=request.GET.get('uname')
    count=User.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def register_hander(request):
    user_name = request.POST['user_name']
    pwd = request.POST['pwd']
    cpwd=request.POST['cpwd']
    email=request.POST['email']
    print(user_name,pwd,cpwd,email)
    if pwd!=cpwd:
        return redirect('register')
    s1=sha1()
    s1.update(pwd.encode('utf8'))
    pwd1=s1.hexdigest()
    print(user_name, pwd1, email)
    user1=User()
    user1.uname=user_name
    user1.upwd=pwd1
    user1.uemail=email
    user1.save()
    return redirect('login')



def login_handler(request):
    ''''''
    username = request.POST['username']
    pwd = request.POST['pwd']
    jizhu=request.POST.get('jizhu',0)
    userlist = User.objects.filter(uname=username)
    if len(userlist)==1:
        s1 = sha1()
        s1.update(pwd.encode('utf8'))
        if s1.hexdigest()==userlist[0].upwd:
            red=render(request,'user/user_center_info.html')
            if jizhu!=0:
                red.set_cookie('uname',username)
            else:
                red.set_cookie('uname',max_age=-1)
            s1=request.session['user_id']=userlist[0].id
            s2=request.session['user_name'] = userlist[0].uname
            return redirect('/user/info')
        else:
            context=({'title':'用户登录','error_name':0,'uname':username,'upwd':pwd})
            return render(request, 'user/login.html', locals())

    else:
        context=({
            'title': '用户登录', 'error_name': 1, 'error_pwd':0, 'uname':username,'upwd': pwd
        })
        return render(request, 'user/login.html', locals())
    # if userlist:
    #     print(userlist)
    #     if pwd1==userlist.upwd:
    #         print("登陆成功")
    #         return render(request, 'user/user_center_info.html')
    #     elif pwd1 != userlist.upwd:
    #         return HttpResponse("密码错误")
    #     return redirect('login')
    # else:
    #     "没找到用户"
    #     return redirect('login')

def user_info(request):
    user_id=request.session['user_id']
    user_phone=User.objects.get(id=user_id).uphone
    user_address=User.objects.get(id=user_id).uaddress
    user_name=User.objects.get(id=user_id).uname
    print(user_id,user_name,user_address,user_phone)
    context = ({
        'title': '用户中心', 'user_phone': user_phone, 'user_name': user_name, 'user_address': user_address
    })
    return render(request,'user/user_center_info.html',context)

def user_order(request):
    title="用户订单"
    return render(request,'user/user_center_order.html',locals())

def user_site(request):
    uid=request.session['user_id']
    user=User.objects.get(id=uid)
    if request.method=='POST':
        user.ureceiver=request.POST.get('ureceiver')
        user.uaddress=request.POST.get('uaddress')
        user.uzipcode=request.POST.get('uzipcode')
        user.uphone=request.POST.get('uphone')
        user.save()
    context={'title':'用户中心','user':user,}
    return render(request,'user/user_center_site.html',context)

