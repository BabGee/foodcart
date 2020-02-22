from django.db import models

class Restaurant(models.Model):
    image = models.ImageField(default='defalt.jpg', upload_to='restaurant_pics')
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    website = models.URLField(default='')

    def __str__(self):
        return f'{self.name}, Location {self.location}'
