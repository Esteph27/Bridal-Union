from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from . import views


urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('', views.ViewHome.as_view(), name='home'),
    path('discover-designer/', views.ViewDiscoverDesigners.as_view(), name='post_detail'),
    path('designer/', views.ViewDesigner.as_view(), name='view_designers'),
    path('designer-portfolio/', views.ViewDesignerPortfolio.as_view(), name='view_portfolio'),
    path('booking/', views.ViewBooking.as_view(), name='view_booking'),
    path('login/', views.ViewLogin.as_view(), name='login'),
    path('customer-account/', views.ViewCustomerAccount.as_view(), name='view_account'),
]
