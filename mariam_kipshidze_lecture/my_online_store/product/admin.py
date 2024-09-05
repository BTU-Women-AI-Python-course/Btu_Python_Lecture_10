from django.contrib import admin

from product.models import Product, Category, Cart, Brand, Tag

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Brand)
admin.site.register(Tag)
