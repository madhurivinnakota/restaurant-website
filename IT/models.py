from django.db import models

class Person(models.Model):
    SHIRT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    ]
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

class Orders(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    descrion = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
