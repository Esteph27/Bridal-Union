from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from . import views


urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('', views.ViewHome.as_view(), name='home'),
    path('about/', views.ViewAbout.as_view(), name='about'),
    # designers 
    path('discover_designers/', views.ViewDiscoverDesigners.as_view(), name='discover_designers'),
    path('<slug:slug>/', views.ImagePostDetail.as_view(), name='imagepost_detail'),
    path('like/<slug:slug>/', views.ImagePostLike.as_view(), name='imagepost_like'),
    path('designer_profile/<pk>/', views.ViewDesigner.as_view(), name='view_designer_profile'),
    # user account
    path('customer_account/', views.ViewCustomerAccount.as_view(), name='view_account'),
]
