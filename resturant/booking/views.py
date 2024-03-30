from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TableBookingForm
from .models import ResturantModel, TableBookingModel

def TableBookingView(request):
    if request.method == 'GET':
        restaurant_name = request.GET.get("restaurant")
        try:
            restaurant_model = ResturantModel.objects.get(name=restaurant_name)
            request.session['restaurant_name'] = restaurant_name  # Store restaurant name in session
            print("Name:", restaurant_name)
            print("Model:", restaurant_model)
        except ResturantModel.DoesNotExist:
            # Handle the case where the restaurant is not found
            print("Restaurant not found")
            restaurant_model = None
        form = TableBookingForm()
    elif request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            restaurant_name = request.session.get('restaurant_name')  # Retrieve restaurant name from session
            try:
                restaurant_model = ResturantModel.objects.get(name=restaurant_name)
                print("Restaurant found in session:", restaurant_model)
            except ResturantModel.DoesNotExist:
                print("Restaurant not found in session")
                restaurant_model = None

            if restaurant_model:
                user = request.user
                date = form.cleaned_data['date']
                people = form.cleaned_data['people']
                booking_name = form.cleaned_data['booking_name']
                booking = TableBookingModel.objects.create(user=user, restaurant=restaurant_model, booking_name=booking_name, date=date, people=people)
                return redirect('restaurant')  # Redirect to the appropriate URL after form submission

    return render(request, "booking/booking_page.html", {"form": form})

def DisplayBookingView(request):
    if request.user.is_staff:
        bookings = TableBookingModel.objects.all()
    else:
        bookings = TableBookingModel.objects.filter(user=request.user)
    return render(request,"booking/booking_list.html",{"bookings":bookings})

def DeleteBookingView(request, id):
    try:
        booking_model = TableBookingModel.objects.get(id=id).delete()
        return redirect("userlistbook")
    except:
        print("Booking ID not found")
    

def EditBookingView(request, id, restaurant):
    booking_model = TableBookingModel.objects.get(id=id)
    restaurant_model = booking_model.restaurant
    if request.method == "POST":
        form = TableBookingForm(request.POST, instance=booking_model)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.restaurant = restaurant_model
            form.save()
            return redirect('userlistbook')
    else:
        form = TableBookingForm(instance=booking_model)
    return render(request, "booking/booking_page.html", {"form": form})
