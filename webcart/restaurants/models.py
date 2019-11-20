from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    #menu_url = models.UrlField(default="http://127.0.0.1:8000/")

    def __str__(self):
        return f'{self.name}, Location {self.location}'
