# myapp/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class user(models.Model):
    nom=models.CharField(max_length=255,null=False)
    age=models.IntegerField(max_length=2,null=True)

    def __str__(self):
        return self.nom
    
