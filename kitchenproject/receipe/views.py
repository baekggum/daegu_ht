from django.shortcuts import render
from .models import Recipe
from blog.models import User
from search import search_recipe
# Create your views here.

def menulist(request):
    user=User.objects.get(name='test')
    recipes=search_recipe(user)
    num=1
    while len(recipes)==0:
        print("num:",num)
        recipes=search_recipe(user,num)
        print(recipes)
        num+=1
    all_recipe={'recipe_list':recipes,'num':num-1}
    return render(request,'menulist.html',all_recipe)