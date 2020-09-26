from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('refrigerator/', views.update,name="refrigerator"),
    #path('detail/<int:recipe_id>/', views.recipe_detail, name="detail"),
    path('update_ingredient/', views.update,name="update"),
    path('update_ingredient/<str:ingredient>/delete', views.delete,name='delete'),
    path('update_ingredient/<str:ingredient>/edit', views.edit, name='edit'),
    path('update_ingredient/seasoning_update', views.seasoning_update, name='seasoning_update'),
    path('base/', views.base, name="base"),
    path('mypage/', views.mypage, name="mypage"),
    path('', views.index, name="index"),
]

