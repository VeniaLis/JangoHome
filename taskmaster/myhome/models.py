from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    pages_number = models.IntegerField(default=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(null=True, blank=True)