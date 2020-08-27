#-*- coding:utf-8 -*-
import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kitchenproject.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from blog.models import User
User(name='test',food_seasoning=['소금','후추'],food_ingredient={'당근':'2020.8.23'}).save()
for i in User.objects.all():
    print(i.food_ingredient['당근'])
