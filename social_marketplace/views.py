from django.shortcuts import render
from django.views import generic, View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
# from django.views.generic.edit import FormView
from .models import Designer, ImagePosts, CustomerAccount


class ViewHome(TemplateView):
    '''render home page template'''

    template_name = 'index.html'


class ViewDiscoverDesigners(ListView):
    '''render discover designers template'''

    model = ImagePosts
    context_object_name = 'image_posts'
    template_name = 'discover_designers.html'


class ViewDesigner(View):
    '''render designer page template and populates with designer model info'''
    model = Designer
    template_name = 'designer.html'

    def get(self, request, designer_id, *args, **kwargs):
        """ get """
        designer = Designer.objects.get(id=designer_id)
        return render(request, self.template_name, {'designer': designer})


class ViewCreateAccount(CreateView):
    '''render create account template'''

    template_name = 'create_account.html'
    model = CustomerAccount
    fields = '__all__'


# ------------ CLASS VIEWS LEFT TO DO

class ViewDesignerPortfolio(TemplateView):
    '''render designer portfolio template'''

    template_name = 'designer_portfolio.html'


class ViewLogin(TemplateView):
    '''render home page template'''

    template_name = 'login.html'


class ViewBooking(TemplateView):
    '''booking form'''

    template_name = 'booking.html'



class ViewCustomerAccount(TemplateView):
    '''render customer account template'''

    template_name = 'customer_account.html'


