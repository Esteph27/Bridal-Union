from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Designer


class ViewHome(TemplateView):
    '''render home page template'''

    template_name = 'index.html'


class ViewDiscoverDesigners(ListView):
    '''render home discover designers template'''

    template_name = 'discover_designers.html'


class ViewDesigner(TemplateView):
    '''render designer page template and populates with designer model info'''

    model = Designer
    template_name = 'designer.html'


class ViewDesignerPortfolio(TemplateView):
    '''render designer portfolio template'''

    template_name = 'designer_portfolio.html'


class ViewBooking(TemplateView):
    '''render booking page template'''

    template_name = 'booking.html'


class ViewLogin(TemplateView):
    '''render home page template'''

    template_name = 'login.html'


class ViewCreateAccount(TemplateView):
    '''render create account template'''

    template_name = 'create_account.html'


class ViewCustomerAccount(TemplateView):
    '''render customer account template'''

    template_name = 'customer_account.html'

