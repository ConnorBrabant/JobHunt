from django.urls import path
from . import views

""" this is the local urls within this app that correspond
to their function defined in the views folder """
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]