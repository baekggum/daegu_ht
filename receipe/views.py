from django.shortcuts import render
from receipe.models import Recipe
from blog.models import Users
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator
from datetime import datetime,timedelta

# Create your views here.
class Recommend_recipe:
    def __init__(self, need_ingredient, title, author, food_ingredient, picture, link):
        self.need_ingredient=need_ingredient
        self.title=title
        self.author=author
        self.food_ingredient=food_ingredient
        self.picture=picture
        self.link=link

#없는 재료명을 위한 클래스 생성
class Ingredient:
    def __init__(self, ingredient_list):
        try:
            self.one=ingredient_list[0]
        except:
            pass
        try:
            self.two=ingredient_list[1]
        except:
            pass

def choice(request):
    current_user = request.user
    x = Users.objects.get(user=current_user)
    user_ingredient=x.food_seasoning+list(x.food_ingredient.keys())
  
    return render(request,'choice.html',{'user_ingredient':user_ingredient})


def choice_menulist(request,num=0):
    print(request.POST.getlist('answers[]'))
    choice_ingredient=request.POST.getlist('answers[]')
    recommend=[]
    recommendOne=[]
    recommendTwo=[]
    for i in Recipe.objects.all():
        flag=0
        for ingredient in i.food_ingredient:
            if ingredient in choice_ingredient:
                flag+=1
        if flag==len(i.food_ingredient)-num:
            recommend.append(i)
        if flag==len(i.food_ingredient)-num-1:
            recommendOne.append(i)
        if flag==len(i.food_ingredient)-num-2:
            recommendTwo.append(i)        
    return render(request,'choice_menulist.html',{'recommend':recommend,'recommendOne':recommendOne,'recommendTwo':recommendTwo,'choice_ingredient':choice_ingredient})    

def getDateFromTuple(tuple):
    return datetime.strptime(tuple, "%Y-%m-%d")   

def allrecipes(request):
    if 'term' in request.GET:
        qs = Ingredient.objects.filter(name__istartswith=request.GET.get('term'))
        food_ingredient = list()
        for product in qs:
            food_ingredient.append(product.name)
        return JsonResponse(food_ingredient, safe=False)
    recipes = Recipe.objects
    recipes_list = Recipe.objects.all()
    paginator = Paginator(recipes_list,12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
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
        return render(request,'allrecipes.html',{"recipes":recipes,'posts':posts,'all_ingredient':L,'buy_date':buy_date})
    return render(request, 'allrecipes.html',{"recipes":recipes,'posts':posts})

def recipes(request,num=0):
    if 'term' in request.GET:
        qs = Ingredient.objects.filter(name__istartswith=request.GET.get('term'))
        food_ingredient = list()
        for product in qs:
            food_ingredient.append(product.name)
        return JsonResponse(food_ingredient, safe=False)
    ###########################################   
    current_user = request.user
    x = Users.objects.get(user=current_user)
    user_ingredient=x.food_seasoning+list(x.food_ingredient.keys())
    #user_ingredient=['계란','올리브유','명란','아보카도','마요네즈']
    recommend=[]
    recommendOne=[]
    recommendTwo=[]
    temp=[]
    i=0
    for i in Recipe.objects.all():
        flag=len(set(i.food_ingredient)-set(user_ingredient))
        if flag==num:
            recommend.append(i)
        if flag==num+1:
            need_ingredient = list(set(i.food_ingredient) - set(user_ingredient))
            recipe=Recommend_recipe(Ingredient(need_ingredient), i.title, i.author, i.food_ingredient, i.picture, i.link)
            recommendOne.append(recipe)
        if flag==num+2:
            need_ingredient = list(set(i.food_ingredient) - set(user_ingredient))
            recipe=Recommend_recipe(Ingredient(need_ingredient), i.title, i.author, i.food_ingredient, i.picture, i.link)
            recommendTwo.append(recipe)   
    ###########################################
    # recipes = Recipe.objects
    # recipes_list = Recipe.objects.all()
    paginator = Paginator(recommend,12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    ###########################################
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
        return render(request,'main_recipe.html',{'recommend':recommend,'recommendOne':recommendOne,'recommendTwo':recommendTwo,'user_ingredient':user_ingredient,'all_ingredient':L,'buy_date':buy_date,'posts':posts})
    return render(request, 'main_recipe.html',{'recommend':recommend,'recommendOne':recommendOne,'recommendTwo':recommendTwo,'user_ingredient':user_ingredient})

def recipes1(request,num=0):
    if 'term' in request.GET:
        qs = Ingredient.objects.filter(name__istartswith=request.GET.get('term'))
        food_ingredient = list()
        for product in qs:
            food_ingredient.append(product.name)
        return JsonResponse(food_ingredient, safe=False)
    ###########################################   
    current_user = request.user
    x = Users.objects.get(user=current_user)
    user_ingredient=x.food_seasoning+list(x.food_ingredient.keys())
    #user_ingredient=['계란','올리브유','명란','아보카도','마요네즈']
    recommend=[]
    recommendOne=[]
    recommendTwo=[]
    temp=[]
    i=0
    for i in Recipe.objects.all():
        flag=len(set(i.food_ingredient)-set(user_ingredient))
        if flag==num:
            recommend.append(i)
        if flag==num+1:
            
            need_ingredient = list(set(i.food_ingredient) - set(user_ingredient))
            recipe=Recommend_recipe(Ingredient(need_ingredient), i.title, i.author, i.food_ingredient, i.picture, i.link)
            recommendOne.append(recipe)
        if flag==num+2:
            need_ingredient = list(set(i.food_ingredient) - set(user_ingredient))
            recipe=Recommend_recipe(Ingredient(need_ingredient), i.title, i.author, i.food_ingredient, i.picture, i.link)
            recommendTwo.append(recipe)   
    ###########################################
    # recipes = Recipe.objects
    # recipes_list = Recipe.objects.all()
    paginator = Paginator(recommendOne,12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    ###########################################
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
        return render(request,'main_recipe_1.html',{'recommend':recommend,'recommendOne':recommendOne,'recommendTwo':recommendTwo,'user_ingredient':user_ingredient,'all_ingredient':L,'buy_date':buy_date,'posts':posts})
    return render(request, 'main_recipe_1.html',{'recommend':recommend,'recommendOne':recommendOne,'recommendTwo':recommendTwo,'user_ingredient':user_ingredient})

def recipes2(request,num=0):
    if 'term' in request.GET:
        qs = Ingredient.objects.filter(name__istartswith=request.GET.get('term'))
        food_ingredient = list()
        for product in qs:
            food_ingredient.append(product.name)
        return JsonResponse(food_ingredient, safe=False)
    ###########################################   
    current_user = request.user
    x = Users.objects.get(user=current_user)
    user_ingredient=x.food_seasoning+list(x.food_ingredient.keys())
    #user_ingredient=['계란','올리브유','명란','아보카도','마요네즈']
    recommend=[]
    recommendOne=[]
    recommendTwo=[]
    temp=[]
    i=0
    for i in Recipe.objects.all():
        flag=len(set(i.food_ingredient)-set(user_ingredient))
        if flag==num:
            recommend.append(i)
        if flag==num+1:
            need_ingredient = list(set(i.food_ingredient) - set(user_ingredient))
            recipe=Recommend_recipe(Ingredient(need_ingredient), i.title, i.author, i.food_ingredient, i.picture, i.link)
            recommendOne.append(recipe)
        if flag==num+2:
            need_ingredient = list(set(i.food_ingredient) - set(user_ingredient))
            recipe=Recommend_recipe(Ingredient(need_ingredient), i.title, i.author, i.food_ingredient, i.picture, i.link)
            recommendTwo.append(recipe)   
    ###########################################

    paginator = Paginator(recommendTwo,12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    ###########################################
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
        return render(request,'main_recipe_2.html',{'recommend':recommend,'recommendOne':recommendOne,'recommendTwo':recommendTwo,'user_ingredient':user_ingredient,'all_ingredient':L,'buy_date':buy_date,'posts':posts})
    return render(request, 'main_recipe_2.html',{'recommend':recommend,'recommendOne':recommendOne,'recommendTwo':recommendTwo,'user_ingredient':user_ingredient})