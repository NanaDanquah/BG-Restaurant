from django import forms
from .models import Booking


class BookingForms(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
