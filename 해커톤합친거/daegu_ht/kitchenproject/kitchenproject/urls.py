from django.contrib import admin
from django.urls import path,include
import blog.views, receipe.views
from django.conf import settings
# 여기있는 url갖고 쓸거기 떄문에

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name="home"),
    path('refrigerator/',blog.views.refrigerator,name="refrigerator"),
    path('accounts/', include('accounts.urls')),
    path('menulist/',receipe.views.menulist,name="menulist"),
    path('refrigerator_update/',blog.views.refrigerator_update,name="refrigerator_update"),
    path('update_ingredient/',blog.views.update,name="update_ingredient"),
    path('update_ingredient/<str:ingredient>/delete',blog.views.delete,name='delete'),
    path('update_ingredient/<str:ingredient>/edit', blog.views.edit, name='edit'),
]
