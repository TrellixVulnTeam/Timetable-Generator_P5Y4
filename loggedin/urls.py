from django.conf.urls import include,url
from . import views


urlpatterns = [

    url(r'^$', views.logg,name='log'),
    url(r'^staff(?P<Staff_No>[0-9]+)/courses', include('Courses.urls'),name= 'SC'),
    url(r'^(?P<STDN>[0-9]+)/courses', include('Courses.urls'), name='course'),


]


