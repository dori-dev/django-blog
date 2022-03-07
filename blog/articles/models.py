from textwrap import wrap
from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize
from django.utils.translation import gettext as _

class Article(models.Model):
    title: str = models.CharField(max_length=256)
    slug = models.SlugField()
    body: str = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def snippet(self):
        return " ".join(self.body[:70].split()[:-1]) + " ..."

    def get_date(self):
        time = humanize.naturaltime(self.date).replace(",", " and").replace(".", "")
        return " ".join(_(word) for word in time.split())

    def get_title(self):
        return "\n".join(wrap(self.title, width=50))

    def __str__(self):
        return self.title
    