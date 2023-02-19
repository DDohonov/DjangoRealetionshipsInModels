from django.db import models

# Create your models here.
class Posts(models.Model):
    user_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to= "posts/")
    description = models.TextField(max_length=1000)
    

class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)