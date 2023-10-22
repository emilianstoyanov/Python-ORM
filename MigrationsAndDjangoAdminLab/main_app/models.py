from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    supplier = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited_on = models.DateTimeField(auto_now=True)
    # barcode = models.IntegerField()
    barcode = models.CharField(max_length=10, blank=True, null=True)
