from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.TextField(blank=False)
    author = models.CharField(max_length=20, blank=False)
    time = models.DateTimeField(auto_now_add=True, blank=False)
    parent_id = models.IntegerField(blank=False)