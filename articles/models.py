"""article modles
"""
from textwrap import wrap
from django.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize
from django.utils.translation import gettext as _


class Article(models.Model):
    title: str = models.CharField("عنوان", max_length=256)
    slug = models.SlugField("آدرس", unique=True, allow_unicode=True)
    body: str = models.TextField("متن")
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField("عکس", default='default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def snippet(self):
        return wrap(self.body[:70], width=60)[0] + " ..."

    def get_date(self):
        time = humanize.naturaltime(self.date)
        if time in ["now", "الان"]:
            return "الان"
        time = time.\
            replace(",", " and").\
            replace(".", "").\
            replace("،", " and ").\
            replace("ها", "").\
            replace("  ", " ").\
            replace("ago", "")
        time = time.split("and")[0].strip()
        time = f"{time} ago"
        return " ".join(_(word) for word in time.split())

    def get_title(self):
        return "\n".join(wrap(self.title, width=50))

    def __str__(self):
        return self.title
