from django.shortcuts import render
from django.contrib.auth.models import User

from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, FormView
    )

from .models import Designer, ImagePosts


class ViewHome(TemplateView):
    '''
    render index template
    '''

    template_name = 'index.html'


class ViewDiscoverDesigners(ListView):
    '''
    render discover designers template
    '''

    model = ImagePosts
    context_object_name = 'image_posts'
    template_name = 'discover_designers.html'


class ViewDesigner(DetailView):
    '''
    render designer profile template and populate with designer model info
    '''

    model = Designer
    template_name = 'designer_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        images = ImagePosts.objects.filter(designer=self.kwargs['pk'])
        context["images"] = images

        return context


class ViewCustomerAccount(TemplateView):
    '''render customer account template'''

    template_name = 'customer_account.html'


# ------------ CLASS VIEWS LEFT TO DO


class ViewBooking(TemplateView):
    '''booking form'''

    template_name = 'booking.html'
