from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Users
from receipe.models import Ingredient
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from collections import OrderedDict 
from datetime import datetime,timedelta
from receipe.models import Recipe

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
    current_user = request.user
    x = Users.objects.get(user=current_user)
    diction=x.food_ingredient
    x.food_ingredient=sorted(diction.items(), key = lambda x:datetime.strptime(x[1], '%Y-%m-%d'), reverse=False)
    context={
            "name": x.user,
            "food_ingredient": x.food_ingredient,
            "food_seasoning": x.food_seasoning,
            }

    return render(request,"refrigerator.html",context=context)

def seasoning_update(request):
    current_user=request.user
    x=Users.objects.get(user=current_user)
    if request.method=="GET": 
        seasoning_name=request.GET['seasoning_name']
        # x.food_seasoning[request.POST['seasoning_name']]
        x.food_seasoning.append(seasoning_name)
        x.save()
        return redirect('update_ingredient')
    else:
        return render(request,'udpate_ingredient.html')             

def update(request):
    if 'term' in request.GET:
        qs = Ingredient.objects.filter(name__istartswith=request.GET.get('term'))
        food_ingredient = list()
        for product in qs:
            food_ingredient.append(product.name)
        return JsonResponse(food_ingredient, safe=False)
    current_user=request.user
    buy_date=datetime.today().strftime("%Y-%m-%d")
    x=Users.objects.get(user=current_user)
    if request.method=="POST": 
        ingredient_name=request.POST['ingredient_name']
        valid_date=datetime.strptime(request.POST['date'],'%Y-%m-%d')
        if ingredient_name=='감자':
            valid_date+=timedelta(days=4)
        elif ingredient_name=='당근':
            valid_date+=timedelta(weeks=2)
        elif ingredient_name=='무':
            valid_date+=timedelta(weeks=1)
        elif ingredient_name=='양배추':
            valid_date+=timedelta(weeks=1) 
        elif ingredient_name=='상추' or ingredient_name=='깻잎':
            valid_date+=timedelta(days=3)
        elif ingredient_name=='피망':
            valid_date+=timedelta(days=3) 
        elif ingredient_name=='양파':
            valid_date+=timedelta(days=4)
        elif ingredient_name=='오이':
            valid_date+=timedelta(weeks=1)
        x.food_ingredient[request.POST['ingredient_name']]=valid_date.strftime("%Y-%m-%d")
        x.save()
        return redirect('allrecipes')
    else:
        sorted_ingredient=sorted(x.food_ingredient.items(), key=lambda x: getDateFromTuple(x[1]), reverse=False)
        origin=datetime.strptime(sorted_ingredient[0][1],"%Y-%m-%d")
        first=[]
        second=[]
        third=[]
        final=[]
        for name,date in sorted_ingredient:
            if name=='' or date=='':
                continue
            date=datetime.strptime(date, "%Y-%m-%d")
            if origin+timedelta(weeks=1)>date:
                first.append((name,date.strftime("%Y-%m-%d")))
            elif origin+timedelta(weeks=2)>date:
                second.append((name,date.strftime("%Y-%m-%d")))
            elif origin+timedelta(weeks=3)>date:
                third.append((name,date.strftime("%Y-%m-%d")))
            else:
                final.append((name,date.strftime("%Y-%m-%d")))
        print(first, second, third, final)
        x.food_seasoning=list(set(x.food_seasoning))
        return render(request,'refrigerator.html',{'first':first,'second':second,'thrid':third,'final':final,'seasoning':x.food_seasoning})


def delete(request, ingredient):
    current_user = request.user
    x=Users.objects.get(user=current_user)
    x.food_ingredient.pop(ingredient)
    x.save()
    return redirect('update')

def edit(request, ingredient):
    current_user = request.user
    x=Users.objects.get(user=current_user)
    valid_date=x.food_ingredient[ingredient]
    if request.method == "POST":
        valid_date=request.POST['date']
        x.food_ingredient[ingredient]=valid_date
        x.save()
        return redirect('update')
    else:
        return render(request, 'edit_ingredient.html',{'ingredient':ingredient, 'valid_date':valid_date})

def getDateFromTuple(tuple):
    return datetime.strptime(tuple, "%Y-%m-%d")      



def recipe_detail(request,recipe_id):
    details = get_object_or_404(Recipe,pk=recipe_id)
    return render(request, 'recipe_detail.html',{'details':details})

def base(request):
    return render(request, 'base.html')

def base1(request):
    return render(request, 'base1.html')

def mypage(request):
    return render(request, 'mypage.html')

def index(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'index.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                Users.objects.create(user=user,name=user,food_seasoning=['소금','후추',' 설탕'],food_ingredient={"계란":'2020-8-30'})
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'index.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'index.html')
    return render(request, 'index.html')

