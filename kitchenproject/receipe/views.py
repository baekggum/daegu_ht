from django.shortcuts import render
from receipe.models import Recipe
from blog.models import Users
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def menulist(request):
    current_user = request.user
    x = Users.objects.get(user=current_user)
    user_ingredient=x.food_ingredient
    #user_ingredient=['계란','올리브유','명란','아보카도','마요네즈']
    recommend=[]
    for i in Recipe.objects.all():
        flag=0
        for ingredient in i.food_ingredient:
            if ingredient in user_ingredient:
                flag+=1
                pass
            else:
                break
        if flag==len(i.food_ingredient):
            recommend.append(i)
    print(recommend)
    for m in recommend:
        context={
        "food_ingredient":user_ingredient,
        "recommend": recommend[m]
        }       
    return render(request,'menulist.html',context=context)
