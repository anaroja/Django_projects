from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    # url(r'^reset$', views.reset),
    url(r'^$', views.index),
    url(r'^main$', views.main),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^clear$', views.clear),
]
