from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def login(request):
    return render(request,'blog/login.html')

def main(request):
    return render(request,'blog/main.html')

def signup(request):
    return render(request,'blog/signup.html')