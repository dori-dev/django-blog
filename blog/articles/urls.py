from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.articles_list, name="list"),
    path("<slug>", views.article_detail),
]
