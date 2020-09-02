# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kitchenproject.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from receipe.models import Recipe, Ingredient
from blog.models import Users
#web_url="http://www.10000recipe.com/recipe/6912736"
def crawling(web_url):
    html = urlopen(web_url)  
    bsObject = BeautifulSoup(html, "html.parser") 
    #print(bsObject)
    #print(bsObject.find('script'))

    bsObject=str(bsObject)
    #print(type(bsObject))
    #ingredient=re.findall('[[]재료[]].*',bsObject)
    start=bsObject.index("application")
    end=bsObject.index("</script>",start)
    dic=eval(bsObject[start+len('application/ld+json">'):end])
    title=dic['name']
    author=dic['author']['name']
    food_ingredient=dic['recipeIngredient']
    for i in range(len(food_ingredient)):   
        ingredient=food_ingredient[i]
        food_ingredient[i]=re.findall('[가-힣\s]+',ingredient)[0].rstrip()
    picture=dic['image'][0]
    link=web_url
    return {'title':title, 'author':author, 'food_ingredient':food_ingredient, 'picture':picture, 'link':link}

if __name__=='__main__':
    Ingredient.objects.all().delete()
    Recipe.objects.all().delete()
    all_ingredient=[]
    for i in range(6912546,6913046):
        web_url="http://www.10000recipe.com/recipe/"+str(i)
        try:
            blog_data_dict = crawling(web_url)
        except:
            continue
        try:
            Recipe.objects.get(title=blog_data_dict['title'])
            continue
        except:
            pass
        ingredient=blog_data_dict['food_ingredient']
        new_ingredient=[]
        for j in ingredient:
            if '적당히' in j:
                L=j.split('적당히')
                j=L[0].strip()
            elif '한 컵' in j:
                L=j.split('한 컵')
                j=L[0].strip()
            elif '길이로 자른' in j:
                L=j.split('길이로 자른')
                j=L[1].strip()
            elif '톡톡톡톡톡' in j:
                L=j.split('톡톡톡톡톡')
                j=L[0].strip()
            elif '흰부분' in j:
                L=j.split('흰부분')
                j=L[0].strip()
            elif '간것' in j:
                L=j.split('간것')
                j=L[0].strip()
            elif '줄기' in j:
                L=j.split('줄기')
                j=L[0].strip()
            elif '깐' in j:
                L=j.split('깐')
                j=L[1].strip()
            elif '흰대' in j:
                L=j.split('흰대')
                j=L[0].strip()
            elif '째끔' in j:
                L=j.split('째끔')
                j=L[0].strip()
            elif '구운' in j:
                L=j.split('구운')
                j=L[1].strip()
            elif '넉넉하게' in j:
                L=j.split('넉넉하게')
                j=L[0].strip()
            elif '농도에맞게' in j:
                L=j.split('농도에맞게')
                j=L[0].strip()
            elif '톡톡' in j:
                L=j.split('톡톡')
                j=L[0].strip()
            elif '삶은' in j:
                L=j.split('삶은')
                j=L[1].strip()
            elif '흰자' in j:
                L=j.split('흰자')
                j=L[0].strip()
            elif '데친' in j:
                L=j.split('데친')
                j=L[1].strip()
            elif '돈까스용' in j:
                L=j.split('돈까스용')
                j=L[1].strip()
            elif '볶은' in j:
                L=j.split('볶은')
                j=L[1].strip()
            elif '넉넉히' in j:
                L=j.split('넉넉히')
                j=L[0].strip()
            elif '바른닭고기' in j:
                L=j.split('바른닭고기')
                j=L[1].strip()
            elif '썬' in j:
                L=j.split('썬')
                j=L[1].strip()
            elif '저염' in j:
                L=j.split('저염')
                j=L[1].strip()
            elif '다진' in j:
                L=j.split('다진')
                j=L[1].strip()
            elif '또는' in j:
                L=j.split('또는')
                j=L[0].strip()
            elif '약간' in j:
                L=j.split('약간')
                j=L[0].strip()
            elif '조금' in j:
                L=j.split('조금')
                j=L[0].strip()
            elif '적당량' in j:
                L=j.split('적당량')
                j=L[0].strip()
            elif '노른자' in j:
                if j=='노른자':
                    j='달걀'
                else:
                    L=j.split('노른자')
                    j=L[0].strip()
            elif '취향껏' in j:
                L=j.split('취향껏')
                j=L[0].strip()
            elif '시판' in j:
                L=j.split('시판')
                j=L[1].strip()    
            elif '밥' in j:
                continue
            elif '얼음' in j:
                continue
            elif '물' in j:
                continue
            elif '찬물' in j:
                continue               
            elif '' == j:
                continue
                       
            new_ingredient.append(j)
            all_ingredient.append(j)
        new_ingredient=list(set(new_ingredient))  
        print(blog_data_dict['food_ingredient'])
        print(new_ingredient)
        Recipe(title=blog_data_dict['title'],author=blog_data_dict['author'],food_ingredient=new_ingredient,
        picture=blog_data_dict['picture'], link=blog_data_dict['link']).save()
    all_ingredient=list(set(all_ingredient))    
    for i in all_ingredient:
        Ingredient(name=i, type=False).save()    
    #Recipe.objects.all().delete()