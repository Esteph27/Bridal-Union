from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from . import views


urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('', views.ViewHome.as_view(), name='home'),
    path('discover_designers/', views.ViewDiscoverDesigners.as_view(), name='discover_designers'),
    path('designer_profile/<int:designer_id>/', views.ViewDesigner.as_view(), name='view_designer_profile'),
    path('booking/', views.ViewBooking.as_view(), name='view_booking'),
    path('login/', views.ViewLogin.as_view(), name='login'),
    path('create_account/', views.ViewCreateAccount.as_view(), name='create_account'),
    path('customer_account/', views.ViewCustomerAccount.as_view(), name='view_account'),
]
