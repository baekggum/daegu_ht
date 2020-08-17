from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('account/',include('account.urls')),
    path('recipe/',include('recipe.urls')),
]
