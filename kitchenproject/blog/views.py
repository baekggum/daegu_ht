from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Users
from receipe.models import Ingredient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def refrigerator(request):
    users = Users.objects.all()
    # conn_user = request.user
    # conn_profile = Users.objects.get(name=conn_user)
    # context = {
    #     'food_ingredient':conn_user.food_ingredient,
    # }
    if 'term' in request.GET:
        qs = Ingredient.objects.filter(name__istartswith=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.name)
        return JsonResponse(titles, safe=False)
    return render(request,'refrigerator.html',{"users":users})

@csrf_exempt
def apply(request):
    if request.method == "POST":
        Users.objects.create(
            food_ingredient = request.POST.get('product'))

    return render(request,'refrigerator.html')