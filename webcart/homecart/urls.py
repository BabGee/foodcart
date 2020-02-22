from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homecart-home'),
    path('about_us', views.about, name='homecart-about'),
	path('contact/', views.contact, name='homecart-contact'),
	path('our_team', views.team, name='homecart-team'),
	path('distributors', views.distributors, name='view_distributors'),
	path('menu', views.viewMenu, name='view_menu'),
	]