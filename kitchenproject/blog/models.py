from django.db import models
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    pub_date=models.DateTimeField('date published')
    seasoning=models.BooleanField(default=False)
    
        
class User(models.Model):
    food_ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
# 조미료랑 식재료 구분은 위의 Ingredient_seasoning True/False로 구분

def __str__(self): 
    return self.title


