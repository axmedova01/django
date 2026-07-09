from django.urls import path
from .views import create_todo, read_todo, update_todo, delete_todo, list_todos

urlpatterns = [
    path('', create_todo, name='create_todo'),
    path('<int:todo_id>/', read_todo, name='read_todo'),
    path('update/<int:todo_id>/', update_todo, name='update_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('list/', list_todos, name='list_todos'),
]
