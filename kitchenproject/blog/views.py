from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import User

# Create your views here.
def home(request):
    return render(request,'home.html')


def refrigerator(request):
    return render(request,'refrigerator.html')