from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date_published')
    
class Recipe(models.Model):
    title = models.CharField(max_length=200)    # 저자
    author = models.CharField(max_length=50)    # 
    food_ingredient = models.ManyToManyField(Ingredient)
    picture = models.ImageField(blank=True)
    link = models.URLField(max_length=255)

    def __str__(self):
        return self.title
