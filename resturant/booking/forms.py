from django import forms
from .models import TableBookingModel


class TableBookingForm(forms.ModelForm):

    booking_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'id':'id_date_field'}))
    people = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','id':'id_integer_field'}))

    class Meta:
        model = TableBookingModel
        fields = ("date","people","booking_name")