from django.shortcuts import render, redirect
from django.urls import reverse
from products.models import Product
from restaurants.models import Restaurant

def home(request):
	context = {
		"restaurants": Restaurant.objects.all()
        }
	return render(request, 'homecart/index.html', context)

def about(request):
	return render(request, "homecart/about.html")

def contact(request):
	return render(request, "homecart/contact.html")    

def team(request):
	return render(request, "homecart/team.html")

def distributors(request):
	context = {
		"distributors": Restaurant.objects.all()
	}
	return render(request, "homecart/distributors.html")

def viewMenu(request):
	context = {
		"object_list": Product.objects.all(),
	}
	return render(request, "homecart/menu.html")

def viewMenuDacofee(request):
	context = {
		"menu_list": Product.objects.filter(restaurant__name='DaCoffee'),
	}
	return render(request, "homecart/menuDacoffee.html")

def viewMenuVogue(request):
	context = {
		"menu_list": Product.objects.filter(restaurant__name='Vogue'),
	}
	return render(request, "homecart/menuVogue.html")

def viewMenuBibo(request):
	context = {
		"menu_list": Product.objects.filter(restaurant__name='Bibo Lounge'),
	}
	return render(request, "homecart/menuBibo.html")

def viewMenuMakuti(request):
	context = {
		"menu_list": Product.objects.filter(restaurant__name='Makuti Villa'),
	}
	return render(request, "homecart/menuMakuti.html")

def viewMenuDotPyzza(request):
	context = {
		"menu_list": Product.objects.filter(restaurant__name='Dot Pyzza'),
	}
	return render(request, "homecart/menuDotpyzza.html")

def viewMenuTitanic(request):
	context = {
		"menu_list": Product.objects.filter(restaurant__name='Titanic Hotel'),
	}
	return render(request, "homecart/menuTitanic.html")

def viewMenuMnarani(request):
	context = {
		"menu_list": Product.objects.filter(restaurant__name='Mnarani Club'),
	}
	return render(request, "homecart/menuMnarani.html")

def viewMenuDapot(request):
	context = {
		"menu_list": Product.objects.filter(restaurant__name='DaPot Villa'),
	}
	return render(request, "homecart/menuDapot.html")


def viewMenuCreek(request):
	context = {
		"menu_list": Product.objects.filter(restaurant__name='Creek Lounge'),
	}
	return render(request, "homecart/menuCreek.html")
