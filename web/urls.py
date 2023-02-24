from django.urls import path
from web import views

urlpatterns = [
    path('home', views.home, name='home'),
]
