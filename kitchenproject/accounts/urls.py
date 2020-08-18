from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD:hackathon/blog/urls.py
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('account/',include('account.urls')),
    path('recipe/',include('recipe.urls')),
]
=======
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
>>>>>>> 016d8a5a3e36b6fe8345826e0060332043ffccde:kitchenproject/accounts/urls.py
