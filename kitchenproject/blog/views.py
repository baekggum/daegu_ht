from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import User
from receipe.models import Ingredient
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')


def refrigerator(request):
    if 'term' in request.GET:
        qs = Ingredient.objects.filter(name__istartswith=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.name)
        return JsonResponse(titles, safe=False)
    return render(request,'refrigerator.html')