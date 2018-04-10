from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^amadon$', views.amadon),  
    url(r'^amadon/buy$', views.order),  
    url(r'^amadon/checkout$', views.checkout), 
    url(r'^amadon/clear$', views.clear), 
]
