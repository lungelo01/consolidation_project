from django.urls import path
from . import views


"""Roots the view 'home' to the url.py file

"""

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
]