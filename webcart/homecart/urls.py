from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homecart-home'),
    path('about_us', views.about, name='homecart-about'),
	path('contact/', views.contact, name='homecart-contact'),
	path('our_team', views.team, name='homecart-team'),
	path('distributors', views.distributors, name='view_distributors'),
	path('menu', views.viewMenu, name='view_menu'),
	path('dacoffee_menu', views.viewMenuDacofee, name='view_menu_dacoffee'),
	path('vogue_menu', views.viewMenuVogue, name='view_menu_vogue'),
	path('bibo_menu', views.viewMenuBibo, name='view_menu_bibo'),
	path('makuti_menu', views.viewMenuMakuti, name='view_menu_makuti'),
	path('dotpyzza_menu', views.viewMenuDotPyzza, name='view_menu_DotPyzza'),
	path('titanic_menu', views.viewMenuTitanic, name='view_menu_titanic'),
	path('mnarani_menu', views.viewMenuMnarani, name='view_menu_mnarani'),
	path('dapot_menu', views.viewMenuDapot, name='view_menu_dapot'),
	path('creek_menu', views.viewMenuCreek, name='view_menu_creek'),
	]