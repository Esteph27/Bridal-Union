from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from .models import Booking, CustomerProfile
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
            messages.success(request, 'Thank you for booking. You can view the status of your booking in your account.')
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
    display customer's profile and bookings
    '''

    profile = get_object_or_404(CustomerProfile, user=request.user)
    bookings = profile.customer.all()

    template = 'customer_profile.html'

    context = {
        'profile': profile,
        'bookings': bookings,
    }

    return render(request, template, context)


@login_required
def edit_booking(request, booking_id):
    '''
    get customer booking and save changes
    '''

    get_booking = get_object_or_404(Booking, booking_id=booking_id)

    template = 'edit_booking.html'
    context = {
        'get_booking': get_booking,
        'from_profile': True,
    }

    return render(request, template, context)
