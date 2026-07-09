from django.contrib import admin
from django.urls import path
from main.views import get_token, goods, new_good

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_token/', get_token, name='get_token'),
    path('goods/', goods, name='goods'),
    path('new_good/', new_good, name='new_good'),
]