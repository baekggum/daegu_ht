from django import forms
from .models import Users

class PostForm(forms.ModelForm):
    class Meta:
         model=Users
         fields=('food_ingredient','food_seasoning',)