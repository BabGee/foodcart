from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='global-home'),
    path('about', views.about, name='global-about'),
    path('team', views.team, name='global-team'),
    path('shops', views.shops, name='view_shops'),
    path('contact', views.contact, name='global-contact'),
]
