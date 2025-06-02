from django.contrib import admin
from .models import Product, ProductImage  # Import your models

admin.site.register(Product)
admin.site.register(ProductImage)
