from django.shortcuts import render

from .models import Product
#from shopping_cart.models import Order

'''
def product_list(request):
	object_list = Product.objects.all()
	filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
	current_order_products = []
	if filtered_orders.exists():
		user_order = filtered_orders[0]
		 user_order_items = user_order.items.all()
		 current_order_products = [product.product for product in user_order_items]
		 context = {
			"object_list": object_list,
			"current_order_products": current_order_products
		}

		return render(request, "foodcart/menu.html", context)

'''
