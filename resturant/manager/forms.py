from django import forms
from list.models import ResturantModel,ResturantMenu,ResturantCuisineModel
from django.conf import settings

class ManagerLoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RestarurantEditForm(forms.ModelForm):

    PRICE_CHOICES = (
        ('$', '1'),
        ('$$', '2'),
        ('$$$', '3'),
        ('$$$$', '4'),
        ('$$$$$', '5'),
    )

    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.ChoiceField(choices=PRICE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_no = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))


    cuisine = forms.MultipleChoiceField(choices=settings.CUISINE_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = ResturantModel
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Get all cuisine choices from settings
            all_cuisines = settings.CUISINE_CHOICES

            # Populate choices for cuisine field
            self.fields['cuisine'].choices = all_cuisines

            # Set initial values for cuisine field based on the cuisines associated with the restaurant
            if self.instance.pk:
                # Get cuisines associated with the restaurant
                restaurant_cuisines = self.instance.resturantcuisinemodel_set.values_list('cuisine', flat=True)
                # Set initial values for cuisine field
                self.initial['cuisine'] = [cuisine for cuisine, _ in all_cuisines if cuisine in restaurant_cuisines]

class MenuEditForm(forms.ModelForm):

    dish = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ResturantMenu
        exclude = ("resturant",)

