from django.shortcuts import render, redirect
from  .forms import ManagerLoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from list.models import ResturantModel,ResturantCuisineModel,ResturantMenuPhoto,ResturantMenu
from .forms import RestarurantEditForm,MenuEditForm

def ManagerLoginView(request):
    if request.method == "POST":
        form = ManagerLoginForm(request.POST)
        print(form.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username+password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    return redirect("restaurant")
                else:
                    # User is not staff
                    messages.error(request, "Please log in with a staff account.")
            else:
                # Authentication failed
                messages.error(request, "Invalid username or password.")
    else:
        form = ManagerLoginForm()
    return render(request, "manager/manager_login.html", {"form": form})
    


def ManagerRestaurantEditView(request):
    restaurant_name = request.GET.get('restaurant')
    restaurant = ResturantModel.objects.get(name=restaurant_name)
    
    if request.method == 'POST':
        form = RestarurantEditForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            restaurant_photo = form.cleaned_data['restaurant_photo']
            form.instance.restaurant_photo = restaurant_photo
            form.save()  # Save changes to the model instance
            cuisines = form.cleaned_data["cuisine"]
            ResturantCuisineModel.objects.filter(resturant=restaurant).delete()
            for cuisine in cuisines:
                preference = ResturantCuisineModel.objects.create(resturant=restaurant,cuisine=cuisine)
            return redirect('restaurant')
    else:
        form = RestarurantEditForm(instance=restaurant)
    
    return render(request, "manager/restaurant_add_edit.html", {"form": form})

def ManagerRestaurantAddView(request):
    print("Entered Add Restaurant")
    if request.method == 'POST':
        form = RestarurantEditForm(request.POST, request.FILES)
        print("form",form.data)
        if form.is_valid():
            restaurant = form.save()
            cuisines = form.cleaned_data["cuisine"]
            for cuisine in cuisines:
                preference = ResturantCuisineModel.objects.create(resturant=restaurant,cuisine=cuisine)
            return redirect('restaurant')
    else:
        form = RestarurantEditForm()

    return render(request,"manager/restaurant_add_edit.html",{"form":form})


def ManagerRestaurantDeleteView(request):
    restaurant_name = request.GET.get('restaurant')
    restaurant_delete = ResturantModel.objects.get(name=restaurant_name).delete()
    return redirect('restaurant')


def ManagerMenuAddView(request):
    restaurant = request.GET.get("restaurant")
    restaurant_model = ResturantModel.objects.get(name=restaurant)
    if request.method == 'POST':
        form = MenuEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.resturant = restaurant_model
            menu = form.save()
            photos = request.FILES.getlist('dish_photos')
            for photo in photos:
                ResturantMenuPhoto.objects.create(dish=menu, dish_photo=photo)
            return redirect('restaurant')
    else:
        form = MenuEditForm()
    return render(request,"manager/menu_add_edit.html",{"form":form})

def ManagerMenuDeleteView(request,id):
    menu_model = ResturantMenu.objects.get(id=id).delete()
    if menu_model is not None:
        return redirect('restaurant')


def ManagerMenuEditView(request,id):
    menu_model = ResturantMenu.objects.get(id=id)
    if request.method == 'POST':
        # If the form is submitted, create a form instance with the submitted data
        form = MenuEditForm(request.POST, request.FILES, instance=menu_model)
        if form.is_valid():
            # If the form is valid, save the form and redirect to a success page or do something else
            form.save()
            photos = request.FILES.getlist('dish_photos')
            ResturantMenuPhoto.objects.filter(dish=menu_model).delete()
            for photo in photos:
                ResturantMenuPhoto.objects.create(dish=menu_model, dish_photo=photo)
            return redirect('restaurant')
        # If the form is not valid, re-render the form with validation errors
    else:
        # If it's a GET request, create a form instance pre-populated with the menu instance data
        form = MenuEditForm(instance=menu_model)
    
    # Render the form in a template
    return render(request, "manager/menu_add_edit.html", {"form": form})