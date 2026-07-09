from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('words_list', views.list, name='list'),
    path('add_word', views.add, name='add')
]
