from django.shortcuts import render
from receipe.models import Recipe
from blog.models import Users
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def menulist(request,num=0):
    current_user = request.user
    x = Users.objects.get(user=current_user)
    user_ingredient=x.food_seasoning+list(x.food_ingredient.keys())
    #user_ingredient=['계란','올리브유','명란','아보카도','마요네즈']
    recommend=[]
    recommendOne=[]
    recommendTwo=[]
    for i in Recipe.objects.all():
        flag=0
        for ingredient in i.food_ingredient:
            if ingredient in user_ingredient:
                flag+=1
        if flag==len(i.food_ingredient)-num:
            recommend.append(i)
        if flag==len(i.food_ingredient)-num-1:
            recommendOne.append(i)
        if flag==len(i.food_ingredient)-num-2:
            recommendTwo.append(i)        
    
    return render(request,'menulist.html',{'recommend':recommend,'recommendOne':recommendOne,'recommendTwo':recommendTwo,'user_ingredient':user_ingredient})