from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize


class Article(models.Model):
    title: str = models.CharField(max_length=256)
    slug = models.SlugField()
    body: str = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def snippet(self):
        return " ".join(self.body[:50].split()[:10]) + " ..."

    def get_date(self):
        return humanize.naturaltime(self.date)  # TODO

    def __str__(self):
        return self.title
