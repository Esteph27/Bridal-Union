from django.shortcuts import render

from .forms import BookingForm


def booking(request):
    '''
    a view to handle bookings
    '''

    booking_form = BookingForm

    template = 'booking.html'
    context = {
        'booking_form': booking_form,
    }

    return render(request, template, context)
