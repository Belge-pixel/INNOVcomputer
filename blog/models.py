from django.db import models
from users.models import User

# Create your models here.

class New(models.Model):
    new_title = models.CharField(max_length=100,null=False)
    new_content = models.TextField()
    new_publication_date = models.DateField(auto_now_add=True)
    new_image = models.ImageField(upload_to='blog_images/',default="")


class Comment(models.Model):
    comment_content = models.TextField()   
    comment_publication_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    new = models.ForeignKey(New,on_delete=models.CASCADE)
    
    def __str__(self):
        return super().__str__()