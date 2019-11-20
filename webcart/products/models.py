from django.db import models
from restaurants.models import Restaurant

class Product(models.Model):
	title = models.CharField(max_length=120)
	price = models.IntegerField()
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None)

	def __str__(self):
		return self.title
