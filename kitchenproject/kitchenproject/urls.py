"""kitchenproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
import blog.views, receipe.views
from django.conf import settings
# 여기있는 url갖고 쓸거기 떄문에

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name="home"),
<<<<<<< HEAD
    path('apply/', blog.views.apply , name='apply'),
=======
>>>>>>> 4c52e637aaa359d98f8fd2689e9aa2dec4b2334f
    path('refrigerator/',blog.views.refrigerator,name="refrigerator"),
    path('accounts/', include('accounts.urls')),
    path('menulist/',receipe.views.menulist,name="menulist"),
]
