from django.shortcuts import render
from .models import ResturantModel

# Create your views here.
def RestaurantListView(request):
    logged_in_user = request.user
    print(logged_in_user)
    sort_by = request.GET.get('sort_by')
    sort_order = request.GET.get('sort_order')

    if sort_by not in ['name', 'price', 'location']:
        sort_by = 'name'
    if sort_order not in ['asc', 'desc']:
        sort_order = 'asc'

    ordering = sort_by
    if sort_order == 'desc':
        ordering = '-' + ordering

    # Get the queryset with sorting applied
    restaurant_list = ResturantModel.objects.all().order_by(ordering)

    print(restaurant_list)
    return render(request,"list/resturants.html",{"restaurant_list":restaurant_list})

def RestaurantView(request):
    restaurant_name = request.GET.get("name")
    restaurant = ResturantModel.objects.get(name=restaurant_name)
    return render(request,"list/resturant_detail.html",{"restaurant":restaurant})