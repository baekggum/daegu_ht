from django.contrib import admin
from django.urls import path,include
from django.conf import settings
# 여기있는 url갖고 쓸거기 떄문에

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('recipe/',include("receipe.urls")),
]