from django.db import models
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def post_by_range(self, start_date, end_date):
        return Post.objects.filter(date__range=(start_date, end_date))


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title
