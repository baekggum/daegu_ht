from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Users
from receipe.models import Ingredient
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def refrigerator(request):
    # blog_detail=get_object_or_404(Users,pk=blog_id)
    current_user = request.user
    x = Users.objects.get(user=current_user)
    context={
            "name": x.user,
            "food_ingredient": x.food_ingredient,
            "food_seasoning": x.food_seasoning,
            }

    return render(request,"refrigerator.html",context=context)

def refrigerator_update(request):
    return render(request,"refrigerator_update.html")    
