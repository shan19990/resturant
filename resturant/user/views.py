from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserDetailsForm
from django.contrib.auth.models import User
from .models import Cuisine
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def UserLoginView(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        print(form.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            print(username)
            try:
                user = User.objects.get(username=username)
                print("User already present")
                login(request, user)
                return redirect("restaurant")  # Redirect to restaurants page after login
            except User.DoesNotExist:
                # Create a new user if one doesn't exist
                user = User.objects.create_user(username=username)
                print("User account has been created")
                login(request, user)
                return redirect("user_details")  # Redirect to user details page after creating account
        else:
            print("Form errors:", form.errors)
    else:
        form = UserLoginForm()

    return render(request, "user/login.html", {"form": form})

def UserDetailsView(request):
    if request.method == "POST":
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            cuisines = form.cleaned_data["cuisine"]
            logged_in_user = request.user
            user_detail = User.objects.get(username=logged_in_user)
            user_detail.first_name = first_name
            user_detail.last_name = last_name
            user_detail.save()
            for cuisine in cuisines:
                preference = Cuisine.objects.create(user=logged_in_user,cuisine=cuisine)
            return redirect("restaurant")
    else:
        form = UserDetailsForm()
    return render(request,"user/user_details.html",{"form":form})
