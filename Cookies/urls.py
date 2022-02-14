

from .views import *
from django.urls import path



urlpatterns = [
    path("home/", home),
    path("abut/", abut),
    path("count/", countviews),


]

