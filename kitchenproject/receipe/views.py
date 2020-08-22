from django.shortcuts import render
# Create your views here.

def menulist(request):
    return render(request,'menulist.html')