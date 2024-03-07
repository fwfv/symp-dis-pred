from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html',views.contact, name = 'contact'),
    path('prediction.html',views.prediction, name = 'prediction'),
    path('about.html',views.about, name = 'about'),
]