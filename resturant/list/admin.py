from django.contrib import admin
from .models import ResturantModel,ResturantCuisineModel,ResturantMenu,ResturantMenuPhoto

# Register your models here.

admin.site.register(ResturantModel)
admin.site.register(ResturantCuisineModel)
admin.site.register(ResturantMenu)
admin.site.register(ResturantMenuPhoto)