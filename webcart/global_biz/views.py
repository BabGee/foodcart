from django.shortcuts import render, redirect
from django.urls import reverse
#from products.models import Product
#from restaurants.models import Restaurant


def home(request):
	context = {
        }
	return render(request, 'global_biz/index.html', context)


def about(request):
	context = {
        }
	return render(request, 'global_biz/about.html', context)


def team(request):
	context = {
        }
	return render(request, 'global_biz/team.html', context)


def shops(request):
	context = {
        }
	return render(request, 'global_biz/shop.html', context)


def contact(request):
	context = {
        }
	return render(request, 'global_biz/contact.html', context)
