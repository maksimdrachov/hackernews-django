from nturl2path import url2pathname
from django.db import models

# Create your models here.
class NewsPost(models.Model):
    title   = models.TextField(max_length=100)
    url     = models.URLField(max_length=300)
    author  = models.TextField(default="No author")
    time    = models.DateTimeField(auto_now_add=True, blank=True)
    votes   = models.IntegerField(default=0)