from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'{self.title} - {self.user}'


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'{self.user} - {self.timestamp}'
