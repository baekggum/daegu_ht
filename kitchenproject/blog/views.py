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
# Create your views here.
def home(request):
    return render(request,'home.html')

def refrigerator(request):
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
        seasoning_name=request.GET('seasoning_name')
        # x.food_seasoning[request.POST['seasoning_name']]
        x.food_seasoning.append('seasoning_name')
        x.save()
        return redirect('refrigerator')
    else:
        return render(request,'refrigerator.html')          

def update(request):
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
        elif ingredient_name=='상추' or '깻잎':
            valid_date+=timedelta(days=3)
        elif ingredient_name=='피망':
            valid_date+=timedelta(days=3) 
        elif ingredient_name=='양파':
            valid_date+=timedelta(days=4)
        elif ingredient_name=='오이':
            valid_date+=timedelta(weeks=1)
        x.food_ingredient[request.POST['ingredient_name']]=valid_date.strftime("%Y-%m-%d")
        x.save()
        return redirect('update_ingredient')
    else:
        sorted_ingredient=sorted(x.food_ingredient.items(), key=lambda x: getDateFromTuple(x[1]), reverse=False)
        L=[]
        first=0
        week=1
        print(sorted_ingredient)
        LL=[]
        for name,date in sorted_ingredient:
            date=datetime.strptime(date, "%Y-%m-%d")
            if first==0:
                first=date
            else:
                pass
            print(week, date, first+timedelta(weeks=week),first+timedelta(weeks=week)>=date)
            if first+timedelta(weeks=week)>=date:
                LL.append((name,date.strftime("%Y-%m-%d")))
                print(LL)
            else:
                L.append(LL)
                LL=[(name,date.strftime("%Y-%m-%d"))]
                week+=1
        L.append(LL)
        print(L)
        return render(request,'update_ingredient.html',{'all_ingredient':L,'buy_date':buy_date})

def delete(request, ingredient):
    current_user = request.user
    x=Users.objects.get(user=current_user)
    x.food_ingredient.pop(ingredient)
    x.save()
    return redirect('update_ingredient')

def edit(request, ingredient):
    current_user = request.user
    x=Users.objects.get(user=current_user)
    valid_date=x.food_ingredient[ingredient]
    if request.method == "POST":
        valid_date=request.POST['date']
        x.food_ingredient[ingredient]=valid_date
        x.save()
        return redirect('update_ingredient')
    else:
        return render(request, 'edit_ingredient.html',{'ingredient':ingredient, 'valid_date':valid_date})

def getDateFromTuple(tuple):
    return datetime.strptime(tuple, "%Y-%m-%d")      

