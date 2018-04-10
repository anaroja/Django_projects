from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    #/handled by method index. renders template that displays current date and time
    url(r'^$', views.index),
    url(r'^time_display/$', views.index)
]
