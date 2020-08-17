from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date_published')

class User(models.Model):
    food_ingredient = models.ManyToManyField(Ingredient)
    food_seasoning = models.CharField(max_length=255)