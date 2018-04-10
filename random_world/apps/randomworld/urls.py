from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^reset$', views.reset),
    url(r'^', views.index),
]
