import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kitchenproject.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from receipe.models import Recipe

user_ingredient=['계란','올리브유','명란','아보카도','마요네즈']
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
        