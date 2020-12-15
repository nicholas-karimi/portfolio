from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='profile-home'),
    # path('contact/', views.contact, name='profile-contact')
]
