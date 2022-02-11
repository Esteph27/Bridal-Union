from . import views
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings


urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico"))),
    path('', views.ViewHome.as_view(), name='home'),
    path('designer/', views.ViewDesigner.as_view(), name='post_detail'),
]
