from django.db import models


class Article(models.Model):
    title: str = models.CharField(max_length=256)
    slug = models.SlugField()
    body: str = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # thumbnail
    # author

    def snippet(self):
        return " ".join(self.body[:80].split()[:10]) + " ..."

    def __str__(self):
        return self.title
