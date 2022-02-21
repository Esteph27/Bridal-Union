from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    '''
    booking form
    '''
    class Meta:
        model = Booking
        fields = (
            'customer_name',
            'customer_email',
            'designer_name',
            'designer_availability',
            'price_range',
            'customer_message',
            )
