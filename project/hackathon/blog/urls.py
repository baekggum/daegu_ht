from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
]
