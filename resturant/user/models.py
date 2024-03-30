from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cuisine(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cuisine = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username