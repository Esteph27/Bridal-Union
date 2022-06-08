from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'booking_date', 'status')
    list_filter = ('booking_date', 'status')
    search_fields = ('status', 'booking_date', 'designer_name')

