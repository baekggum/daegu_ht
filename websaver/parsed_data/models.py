from django.db.models import Model, CharField, URLField
from django_mysql.models import ListCharField
# Create your models here.
class Recipe(Model):
    title=CharField(max_length=200)
    author=CharField(max_length=50)
    food_ingredient=ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=(6 * 11))
    picture=URLField()
    link=URLField()

    def __str__(self):
        return self.title

class Ingredient(Model):
    name=CharField(max_length=20)
    
    def __str__(self):
        return self.name