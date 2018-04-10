from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    # url(r'^reset$', views.reset),
    url(r'^$', views.index),
    url(r'^add_word', views.add_word),
    url(r'^clear', views.clear),
]
