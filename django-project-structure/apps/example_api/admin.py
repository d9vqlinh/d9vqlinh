from django.contrib import admin

from .models import Category, ProductType, Product, ProductColor, ProductSize

admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(ProductSize)
# admin.site.register(UserBase)
