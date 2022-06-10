from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from .models import Booking
from social_marketplace.models import Designer


def booking(request, designer_id):
    '''
    a view to handle bookings
    '''
    user = request.user
    designer = Designer.objects.get(pk=designer_id)
    booking_form = BookingForm

    # get form info
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data.get('customer_name')
            customer_email = form.cleaned_data.get('customer_email')
            designer_name = form.cleaned_data.get('designer_name')
            price_range = form.cleaned_data.get('price_range')
            date_of_wedding = form.cleaned_data.get('date_of_wedding')
            select_date = form.cleaned_data.get('select_date')
            select_time = form.cleaned_data.get('select_time')
            customer_message = form.cleaned_data.get('customer_message')
            BookingForm.save(form)
            messages.success(request, 'Thank you for booking.')

    #get user info to populate filds in form
    if request.user.is_authenticated:
        if request.POST:
            customer = request.user
            customer_name = request.user.username
            booking_form = BookingForm(initial={'customer_name': customer_name})
    else:
        booking_form = BookingForm()

    template = 'booking.html'
    context = {
        'booking_form': booking_form,
        'user': user,
        'designer': designer,
    }

    return render(request, template, context)


@login_required
def customer_profile(request):
    '''
    display customer's profile
    '''

    user = request.user
    customer_name = Booking.objects.filter()
    get_bookings = Booking.objects.filter(customer_name)

    template = 'customer_profile.html'

    context = {
        'user': user,
        'get_bookings': get_bookings,
    }

    return render(request, template, context)