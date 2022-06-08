from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView
    )

from .models import Designer, ImagePosts
from .forms import CommentForm


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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        ''' handle comment form submission '''

        queryset = ImagePosts.objects.filter(status=1)
        image_post = get_object_or_404(queryset, slug=slug)
        comments = image_post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if image_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.image_post = image_post
            comment.save()
            messages.success(request, 'Your comment was sent successfully.')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "imagepost_detail.html",
            {
                "image_post": image_post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),
                "liked": liked,
            },
        )


class ImagePostLike(View):
    '''
    a view to handle likes
    '''

    def post(self, request, slug):
        '''like functionality'''

        image_post = get_object_or_404(ImagePosts, slug=slug)

        if image_post.likes.filter(id=request.user.id).exists():
            image_post.likes.remove(request.user)
        else:
            image_post.likes.add(request.user)

        return redirect(request.META.get('HTTP_REFERER'))



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

