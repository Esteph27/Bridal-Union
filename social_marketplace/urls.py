from . import views
from django.urls import path


urlpatterns = [
    path('', views.ViewHome.as_view(), name='home'),
    path('designer/', views.ViewDesigner.as_view(), name='post_detail'),
]
