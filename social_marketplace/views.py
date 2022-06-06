from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.models import User

from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView
    )

from .models import Designer, ImagePosts


class ViewHome(TemplateView):
    '''
    render index page
    '''

    template_name = 'index.html'


class ViewAbout(TemplateView):
    '''
    render About page
    '''

    template_name = 'about.html'


class ViewDiscoverDesigners(generic.ListView):
    '''
    render discover designers page.
    shows all posts posted by designers via the admin
    '''

    model = ImagePosts
    context_object_name = 'image_posts'
    queryset = ImagePosts.objects.filter(status=1).order_by('-date_posted')
    template_name = 'discover_designers.html'


class ImagePostDetail(View):
    '''
    shows a specific post's details
    '''

    def get(self, request, slug, *args, **kwargs):
        ''' get posts' details '''

        queryset = ImagePosts.objects.filter(status=1)
        image_post = get_object_or_404(queryset, slug=slug)
        comments = image_post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if image_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "imagepost_detail.html",
            {
                "image_post": image_post,
                "comments": comments,
                "liked": liked
            },
        )


class ViewDesigner(DetailView):
    '''
    render a specific designer profile page
    and populate with designer model info
    '''

    model = Designer
    template_name = 'designer_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        images = ImagePosts.objects.filter(designer=self.kwargs['pk'])
        context["images"] = images

        return context




class ViewCustomerAccount(TemplateView):
    '''render customer account page'''

    template_name = 'customer_account.html'

