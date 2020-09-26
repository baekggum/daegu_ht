from django.urls import path
from . import views

urlpatterns = [
    path('allrecipes/', views.allrecipes, name="allrecipes"),
    path('recipes/', views.recipes, name="recipes"),
    path('recipes1/', views.recipes1, name="recipes1"),
    path('recipes2/', views.recipes2, name="recipes2"),
    path('choice/', views.choice, name="choice"),
    path('choice_menulist/', views.choice_menulist, name="choice_menulist"),
]

