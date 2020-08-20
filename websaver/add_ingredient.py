import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from parsed_data.models import Recipe, Ingredient

if __name__=='__main__':
    Ingredient.objects.all().delete()
    all_ingredient=[]
    for i in Recipe.objects.all():
        for j in i.food_ingredient:
            if '약간' in j:
                L=j.split('약간')
                j=L[0].rstrip()
            elif '조금' in j:
                L=j.split('조금')
                j=L[0].rstrip()
            elif '적당량' in j:
                L=j.split('적당량')
                j=L[0].rstrip()
            all_ingredient.append(j)
    all_ingredient=list(set(all_ingredient))
    for i in all_ingredient:
        '''
        if type=='y':
            Ingredient(name=i,type=True).save()
        else:
            Ingredient(name=i,type=False).save()
        '''
        Ingredient(name=i,type=False).save()
    print(Ingredient.objects.all())