from datetime import datetime

from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField()
    content = models.TextField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content
