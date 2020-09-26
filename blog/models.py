from django.db.models import Model, CharField, URLField
from django_mysql.models import ListCharField
from jsonfield import JSONField
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=True)
    name=CharField(default=True,max_length=20)
    food_seasoning=ListCharField(
        default=True,
        base_field=CharField(max_length=10),
        size=20,
        max_length=(20 * 11))
    food_ingredient=JSONField(null = True) #dictionary

    def __str__(self):
        return self.name
