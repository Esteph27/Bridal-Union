from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from .models import Designer


class ViewHome(TemplateView):

    template_name = 'index.html'


class ViewDesigner(generic.ListView):

    model = Designer
    template_name = 'designer.html'
