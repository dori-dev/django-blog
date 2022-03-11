"""blog URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler403, handler404, handler500
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main, name="home"),
    path("about/", views.about, name="about"),
    path("articles/", include("articles.urls")),
    path("accounts/", include("accounts.urls")),
    path("todo/", include("todoapp.urls")),
    path("news/", views.news, name="news"),
    path("<slug>/", views.error),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'blog.views.error'
handler403 = 'blog.views.error'
handler404 = 'blog.views.error'
handler500 = 'blog.views.error'
