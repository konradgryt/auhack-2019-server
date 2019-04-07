from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
