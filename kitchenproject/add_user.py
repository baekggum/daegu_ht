#-*- coding:utf-8 -*-
import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kitchenproject.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from blog.models import Users
from django.contrib.auth.models import User as Account

#Users_name_list 변수를 빈 리스트로 미리 선언 
Users_name_list = [] 

#Users의 이름만 뽑아서, 리스트에 저장
for k in Users.objects.all():
   Users_name_list.append(k.name) 


for x in Account.objects.all():
   # x.username이 Users_name_list에 이미 존재하면, 다시 반복문 실행 
   if x.username in Users_name_list:
       continue 
   else:
       Users(name=x.username,food_seasoning=['소금','후추',' 설탕']).save()