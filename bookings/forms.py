from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('customer_name', 'customer_email', 'designer_name', 
                'price_range', 'date_of_wedding', 'select_date', 
                'select_time','customer_message',)
