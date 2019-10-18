from django.conf.urls import url
from . import views


urlpatterns = [
    url('home$', views.person_details)
]

