from django.db.models import Model, CharField, URLField
from django_mysql.models import ListCharField
from jsonfield import JSONField
# Create your models here.

class Users(Model):
    name=CharField(default=True,max_length=20)
    food_seasoning=ListCharField(
        default=True,
        base_field=CharField(max_length=10),
        size=20,
        max_length=(20 * 11))
    food_ingredient=JSONField() #dictionary

    def __str__(self):
        return self.name

    def get_object(self):
        return self.request.user