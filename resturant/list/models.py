from django.db import models

# Create your models here.

class ResturantModel(models.Model):
    class PriceChoices(models.TextChoices):
        DOLLAR_ONE = '$', '1'
        DOLLAR_TWO = '$$', '2'
        DOLLAR_THREE = '$$$', '3'
        DOLLAR_FOUR = '$$$$', '4'
        DOLLAR_FIVE = '$$$$$', '5'

        def __str__(self):
            return self.value  # Return the dollar sign value when converted to string

    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=264, blank=True, null=True)
    price = models.CharField(max_length=5, choices=PriceChoices.choices, blank=True, null=True)
    description = models.TextField(max_length=264, blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    restaurant_photo = models.ImageField(upload_to='restaurant_photo/', blank=True, null=True, default="")
    
    def __str__(self):
        return self.name
    

class ResturantCuisineModel(models.Model):
    resturant = models.ForeignKey(ResturantModel,on_delete=models.CASCADE,null=True,blank=True)
    cuisine = models.CharField(max_length=20)

    def __str__(self):
        return self.resturant.name
    

class ResturantMenu(models.Model):
    resturant = models.ForeignKey(ResturantModel, on_delete=models.CASCADE,null=True,blank=True)
    dish = models.CharField(max_length=264)
    price = models.IntegerField()

    def __str__(self):
        return self.dish


class ResturantMenuPhoto(models.Model):
    dish = models.ForeignKey(ResturantMenu, on_delete=models.CASCADE,blank=True,null=True)
    dish_photo = models.ImageField(upload_to='dish_photo/', blank=True, null=True, default="")

    def __str__(self):
        return self.dish.dish