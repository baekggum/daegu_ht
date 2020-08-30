from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Users
from receipe.models import Ingredient
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .form import UsersForm
from datetime import datetime, timedelta
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
    current_user = request.user
    x = Users.objects.get(user=current_user)
    if request.method=="POST": #수정정보 입력을 하고나면 저장된다->냉장고화면으로 전환.
        form=UsersForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            x.food_ingredient=form.cleaned_data['food_ingredient']
            x.food_seasoning=form.cleaned_data['food_seasoning']
            x.save()
            return redirect('refrigerator')
    else: #딱 처음 입력받을때 기존정보 보여주며 틀이 화면에 뜬다
        form=UsersForm(instance=x)
        return render(request,'refrigerator_update.html',{'form':form})    

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
        return render(request,'update_ingredient.html',{'all_ingredient':x.food_ingredient.items(),'buy_date':buy_date})

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