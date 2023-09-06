from django.db import models
from django.db.models.fields.files import ImageField


# Create your models here.
class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = ImageField(upload_to='blog_images/')  # Use ImageField instead of FileField
    date_published = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='blog_posts')


    def __str__(self):
        return self.title
