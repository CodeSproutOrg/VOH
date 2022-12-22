import datetime
from django.db import models


class Post(models.Model):
    """ Model of posts """
    title = models.CharField(max_length=20)
    post = models.TextField(null=False)
    time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return f'Post {self.title}'
