from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from . import views


urlpatterns = [
    path('booking/<designer_id>', views.booking, name="booking"),
    path('customer_profile/', views.customer_profile, name="customer_profile"),
    path('edit_booking/<booking_id>/', views.edit_booking, name="edit_booking"),
    path('delete_booking/<booking_id>/', views.delete_booking, name="delete_booking"),
]
