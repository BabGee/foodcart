from django.contrib import admin
from .models import Product, Status, Order, OrderProduct

admin.site.register(Product)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(OrderProduct)
