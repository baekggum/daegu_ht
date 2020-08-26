from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('refrigerator/', views.refrigerator,name="refrigerator"),
    path('recipes/', views.recipes, name="recipes"),
    path('detail/<int:recipe_id>/', views.recipe_detail, name="detail"),
    path('base/', views.base, name="base"),
]

