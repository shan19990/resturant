from django.db import models
from django.contrib.auth.models import User
from list.models import ResturantModel,ResturantCuisineModel

class TableBookingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=False,null=False)
    booking_name = models.CharField(max_length=100,blank=False,null=False,default="")
    restaurant = models.ForeignKey(ResturantModel, on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateField(blank=False,null=False)
    people = models.IntegerField(blank=False,null=False)


    def __str__(self):
        return self.user.username