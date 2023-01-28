from django.db import models

# Create your models here.

class user(models.Model):
    
    email = models.EmailField(unique=True,primary_key=True)
    password = models.CharField(max_length=255)
    profile = models.CharField(max_length=255)
    adblock = models.BooleanField(default=False)
    ProfileDict = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.email