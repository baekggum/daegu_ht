from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=['food_ingredient','food_seasoning']