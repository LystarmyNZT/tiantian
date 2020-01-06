"""tiantian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include


from user.views import register, login, register_hander, login_handler, register_exist, user_info, user_order, user_site


urlpatterns = [
    url(r'^register/$',register,name='register'),
    url(r'^login/$',login,name='login'),
    url(r'^register_handler/$',register_hander,name='register_handler'),
    url(r'^login_handler/$',login_handler,name='login_handler'),
    url(r'^register_exist/$',register_exist,name='register_exist'),
    url(r'^info/$',user_info,name='user_info'),
    url(r'^order/$',user_order,name='user_order'),
    url(r'^site/$',user_site,name='user_site'),
]
