from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    user_image = models.ImageField(upload_to= 'users_images/',default='users_images/profile.png',null=True,blank=True)
    user_location = models.CharField(max_length=20,null=True)
    user_sexe = models.CharField(max_length=1,null=True)
    
    def __str__(self):
        return super().__str__()
    