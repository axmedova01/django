from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_table, name='main_table'),
    path('name', views.name, name='name'),
    path('name/delete/<name_id>/', views.delete_item, name='delete_item'),
    path('name/update/<name_id>/', views.update_item, name='update_item'),
    path('surname', views.surnam, name='surname'),
    path('surname/delete/<s_id>/', views.delete_surname, name='delete_surname'),
    path('surname/update/<s_id>/', views.update_surname, name='update_surname'),
    path('patronymic', views.patronym, name='patronymic'),
    path('patronymic/delete/<pat_id>/', views.delete_patronymic, name='delete_patronymic'),
    path('patronymic/update/<pat_id>/', views.update_patronymic, name='update_patronymic'),
    path('street', views.streets, name='street'),
    path('street/delete/<st_id>/', views.delete_street, name='delete_street'),
    path('street/update/<st_id>/', views.update_street, name='update_street'),
    path('add_main', views.add_main, name='add_main'),
    path('delete/<id>', views.delete_main, name='delete_main'),
    path('update/<id>/', views.update_main, name='update_main'),


]
