#from nturl2path import url2pathname
from django.db import models

# Create your models here.
class NewsPost(models.Model):
    title   = models.CharField(max_length=100, blank=False)
    url     = models.URLField(max_length=300, blank=False)
    author  = models.CharField(max_length=20, blank=False)
    time    = models.DateTimeField(auto_now_add=True, blank=False)
    votes   = models.IntegerField(default=0, blank=False)