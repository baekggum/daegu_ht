from django.db.models import Model, CharField, URLField
from django_mysql.models import ListCharField
from jsonfield import JSONField
# Create your models here.

class User(Model):
    name=CharField(max_length=20)
    food_seasoning=ListCharField(
        base_field=CharField(max_length=10),
        size=20,
        max_length=(20 * 11))
    food_ingredient=JSONField() #dictionary

    def __str__(self):
        return self.name
