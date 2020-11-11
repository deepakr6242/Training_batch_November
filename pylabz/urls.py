from django.urls import path,include
from rest_framework import routers
from django.views.generic import TemplateView
from . import views

urlpatterns = [

    path('',views.index,name= 'index'),
    path(r'validate/', views.validate, name='validate'),
    path(r'contact', views.contact, name='contact'),
    path(r'contact_list', views.contact_list,name= 'contact_list'),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),




]



