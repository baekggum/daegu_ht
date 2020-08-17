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
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from parsed_data.models import Recipe

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
    picture=dic['image']
    link=web_url
    return {'title':title, 'author':author, 'food_ingredient':food_ingredient, 'picture':picture, 'link':link}

if __name__=='__main__':
    for i in range(6912636,6912646):
        web_url="http://www.10000recipe.com/recipe/"+str(i)
        try:
            blog_data_dict = crawling(web_url)
            #print(blog_data_dict)
        except:
            continue
        Recipe(title=blog_data_dict['title'],author=blog_data_dict['author'],food_ingredient=blog_data_dict['food_ingredient'],
        picture=blog_data_dict['picture'], link=blog_data_dict['link']).save()
    #Recipe.objects.all().delete()