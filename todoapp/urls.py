"""todoapp urls
"""
from django.urls import path
from .views import (
    todo_list_view,
    create_todo,
    delete_todo,
    edit_todo,
)

app_name = "todoapp"
urlpatterns = [
    path("", todo_list_view, name="todo_list"),
    path('create/', create_todo, name='create_todo'),
    path('<id_>/delete/', delete_todo, name='delete_todo'),
    path('<id_>/edit/', edit_todo, name="edit_todo"),
]