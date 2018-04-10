from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    #/ - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
    url(r'^$', views.index),  
    #/new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
    url(r'^new/', views.new), 
    #Have this be handled by a method named 'create'.  For now, have this url redirect to /.
    url(r'^create/', views.create),
    #/{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
    url(r'^(?P<number>\w+)$', views.show),
    #/{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'. 
    url(r'^(?P<number>\w+)/edit$', views.edit),
    #/{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /. 
    url(r'^(?P<number>\w+)/delete$', views.destroy),
    #We are adding a form
    url(r'^create$', views.create)
]
