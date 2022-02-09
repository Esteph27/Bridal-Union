from django.shortcuts import render
from django.views import generic 
from .models import Designer


class ViewDesigner(generic.ListView):
    model = Designer 
    template_name = 'designer.html'


