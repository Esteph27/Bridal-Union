from django.contrib import admin
from .models import Booking, CustomerProfile

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    model = Booking

    list_display = ('booking_id', 'booking_date', 'status', 'designer_name',)
    list_filter = ('booking_date', 'status',)
    search_fields = ('status', 'booking_date', 'designer_name',)



@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):

    model = CustomerProfile
    list_display = ('user', 'customer_name',)
    list_filter = ('user', 'customer_name',)