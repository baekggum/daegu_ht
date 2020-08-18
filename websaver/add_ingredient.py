import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from parsed_data.models import Recipe, Ingredient

if __name__=='__main__':
    all_ingredient=[]
    for i in Recipe.objects.all():
        for j in i.food_ingredient:
            all_ingredient.append(j)
    all_ingredient=list(set(all_ingredient))
    for i in all_ingredient:
        Ingredient(name=i).save()
    print(Ingredient.objects.all())