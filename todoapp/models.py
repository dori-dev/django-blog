"""todoapp models"""
from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):
    work = models.CharField("کار", max_length=90)
    checked = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.CharField("زمان(اختیاری)", blank=True,
                            null=True, max_length=50)

    def __str__(self):
        return self.work
