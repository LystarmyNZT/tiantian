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

from goods.views import index, list, detail, search

urlpatterns = [
    url(r'^index',index),
    url(r'^list(\d+)_(\d+)_(\d+)/$',list),
    url(r'^(\d+)/$',detail),
    url(r'^search/$',search,name='search')
]
