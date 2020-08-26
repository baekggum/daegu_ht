from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=['food_seasoning','food_ingredient',]