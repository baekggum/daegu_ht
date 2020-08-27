from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Users
from receipe.models import Ingredient
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .form import UsersForm

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