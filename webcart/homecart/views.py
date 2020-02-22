from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from restaurants.models import Restaurant
from products.models import Product, Order, OrderProduct
#from users.models import Address, Coupon
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View
from django.contrib import messages
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
#from users.forms import CheckoutForm, CouponForm
import random
import string

def home(request):
	products = Product.objects.all()
	restaurants = Restaurant.objects.all()
	context = {
		'offer_products' : products.filter(status__name='Offer')[:2],
		'today_offers' : products.filter(status__name='New'),
		'restaurants': restaurants
        }
	return render(request, 'homecart/index.html', context)

def about(request):
	return render(request, 'homecart/about.html')

def contact(request):
	return render(request, 'homecart/contact.html')    

def team(request):
	return render(request, 'homecart/team.html')

def distributors(request):
	context = {
		'distributors': Restaurant.objects.all()
	}
	return render(request, 'homecart/distributors.html')

def product_detail(request,pk):
    product = Product.objects.get(pk = pk)
    restaurant = product.restaurant
    context = {
        'product': product,
        'restaurant_prod' : Product.objects.filter(restaurant__name=restaurant)
    }
    return render(request, 'homecart/product.html', context)


def restaurant_detail(request,pk):
    rest = Restaurant.objects.get(pk = pk)
    
    context = {
        'products_with_restaurant': Product.objects.filter(restaurant__name = rest),
    }
    
    return render(request, 'globalbiz/rest_menu.html', context)


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'homecart/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, 'You do not have an active order')
            return redirect('/')

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_product, created = OrderProduct.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #check if the order product is in the order
        if order.products.filter(product__pk=product.pk).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, 'This product quantity was updated.')
            return redirect('order-summary')
        else:
            order.products.add(order_product)
            messages.info(request, 'This product was added to your cart.')
            return redirect('order-summary')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
        messages.info(request, 'This product was added to your cart.')
        return redirect('order-summary')

@login_required
def remove_single_product_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        #check if the order product is in the order
        if order.products.filter(product__pk=product.pk).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()
            else:
                order.products.remove(order_product)
            messages.info(request, 'This product quantity was updated.')
            return redirect('order-summary')
        else:
            messages.info(request, 'This product was not in your cart')
            return redirect('product', pk=pk)
    else:
        messages.info(request, 'You do not have an active order')
        return redirect('product', pk=pk)


@login_required
def remove_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        #check if the order product is in the order
        if order.products.filter(product__pk=product.pk).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False
            )[0]
            order.products.remove(order_product)
            messages.info(request, 'This product was removed from your cart.')
            return redirect('order-summary')
        else:
            messages.info(request, 'This product was not in your cart')
            return redirect('product-detail', pk=pk)
    else:
        messages.info(request, 'You do not have an active order')
        return redirect('product-detail', pk=pk)


def viewMenu(request):
	context = {
		'object_list': Product.objects.all(),
	}
	return render(request, 'homecart/menu.html')


