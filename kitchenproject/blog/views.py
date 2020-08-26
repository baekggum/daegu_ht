from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Users
from receipe.models import Ingredient
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def refrigerator(request):
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
