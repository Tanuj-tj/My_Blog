from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=20,default="")
    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.CharField(max_length=130)
    timeStamp = models.DateField(blank=True)
    thumbnail = models.ImageField(upload_to='blog/images',default="")

    def __str__(self):
        return f"{self.title} - {self.author}"


class BlogComment(models.Model):

    sno = models.AutoField(primatu)