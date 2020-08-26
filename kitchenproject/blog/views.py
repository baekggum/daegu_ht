from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Users
from receipe.models import Ingredient,Recipe
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def refrigerator(request):
    if 'term' in request.GET:
        qs = Ingredient.objects.filter(name__istartswith=request.GET.get('term'))
        food_ingredient = list()
        for product in qs:
            food_ingredient.append(product.name)
        return JsonResponse(food_ingredient, safe=False)
    # blog_detail=get_object_or_404(Users,pk=blog_id)
    current_user = str(request.user)
    print(type(current_user))
    print(current_user)
    for x in Users.objects.all():
   # x.username이 Users_name_list에 이미 존재하면, 다시 반복문 실행 
        print(type(x.name))
        if x.name==current_user:
            context={
            "name": x.name,
            "food_ingredient": x.food_ingredient,
            "food_seasoning": x.food_seasoning,
             }
        
    return render(request,"refrigerator.html",context=context)

def recipes(request):
    recipes = Recipe.objects
    recipes_list = Recipe.objects.all()
    paginator = Paginator(recipes_list,12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'main_recipe.html',{"recipes":recipes,'posts':posts})

def recipe_detail(request,recipe_id):
    details = get_object_or_404(Recipe,pk=recipe_id)
    return render(request, 'recipe_detail.html',{'details':details})

def base(request):
    return render(request, 'base.html')