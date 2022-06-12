import uuid
from datetime import date
from django.contrib.auth.models import User
from django.db import models

from social_marketplace.models import Designer


BOOKING_STATUS = (
    ('Confirm Booking', 'Confirm Booking'),
    ('Decline Booking', 'Decline Booking'),
)

PRICES = (
    ('£2,500 - £3,500', '£2,500 - £3,500'),
    ('£3,500 - £4,500', '£3,500 - £4,500'),
    ('£4,500 - £5,500', '£4,500 - £5,500'),
    ('£5,500 - £6,500', '£5,500 - £6,500'),
    ('£6,500 - £7,500', '£6,500 - £7,500'),
    ('£7,500 - £8,500', '£7,500 - £8,500'),
    ('£8,500 - £9,500', '£8,500 - £9,500'),
    ('£9,500 +', '£9,500 +'),
)

TIME_CHOICES = (
    ("08:00", "08:00"),
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
    )


class CustomerProfile(models.Model):
    '''
    Model to store a user's information for their customer account
    '''

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=40, null=True, blank=True)
    customer_email = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    '''
    A model to store customer bookings
    '''

    customer_name = models.ForeignKey(
        CustomerProfile,
        null=True,
        on_delete=models.SET_NULL, related_name='customer'
        )
    customer_email = models.ForeignKey(
        CustomerProfile,
        null=True, blank=True,
        on_delete=models.SET_NULL
        )
    designer_name = models.ForeignKey(
        Designer,
        null=True,
        on_delete=models.SET_NULL,
        related_name='designername'
        )
    price_range = models.CharField(max_length=200, choices=PRICES, default='£2,500 - £3,500')
    date_of_wedding = models.DateField(default=date.today)
    select_date = models.DateField(default=date.today)
    select_time = models.CharField(
        max_length=10, choices=TIME_CHOICES, default='12:00')
    customer_message = models.TextField(max_length=800, blank=True)

    booking_date = models.DateTimeField(auto_now_add=True)
    booking_id = models.CharField(max_length=32, null=False, editable=False, unique=True)
    status = models.CharField(max_length=200, choices=BOOKING_STATUS )
    
    def _booking_id(self):
        """
        create a random and unique order id with uuid
        """
        return uuid.uuid4().hex[:5].upper()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.booking_id:
            self.booking_id = self._booking_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.booking_id)

