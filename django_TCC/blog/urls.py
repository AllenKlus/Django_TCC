from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='TCC_home'),
    path('about/', views.about, name='TCC_about'),
    path('contact/', views.contact, name='TCC_contact'),
]