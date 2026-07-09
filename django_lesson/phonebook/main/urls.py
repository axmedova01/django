from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_table, name='main_table'),
    path('name', views.name, name='name'),
    path('name/delete/<id_name>/', views.delete_name, name='delete_name'),
    path('name/update/<id_name>/', views.update_name, name='update_name'),
    path('fam', views.fam, name='fam'),
    path('fam/delete/<id_fam>/', views.delete_fam, name='delete_fam'),
    path('fam/update/<id_fam>/', views.update_fam, name='update_fam'),
    path('otch', views.otch, name='otch'),
    path('otch/delete/<id_otch>/', views.delete_otch, name='delete_otch'),
    path('otch/update/<id_otch>/', views.update_otch, name='update_otch'),
    path('street', views.streets, name='street'),
    path('street/delete/<id_street>/', views.delete_street, name='delete_street'),
    path('street/update/<id_street>/', views.update_street, name='update_street'),
    path('add_main', views.add_main, name='add_main'),
    path('delete/<id>', views.delete_main, name='delete_main'),
    path('update/<id>/', views.update_main, name='update_main'),
]