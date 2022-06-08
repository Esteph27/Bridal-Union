from django.shortcuts import render

from .forms import BookingForm
from social_marketplace.models import Designer


def booking(request, designer_id):
    '''
    a view to handle bookings
    '''
    user = request.user
    designer = Designer.objects.get(pk=designer_id)
    booking_form = BookingForm
    
    template = 'booking.html'
    context = {
        'booking_form': booking_form,
        'user': user,
        'designer': designer,
    }

    return render(request, template, context)
