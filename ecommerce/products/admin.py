from django.contrib import admin
from products.models import Product
from products.models import Customer  # Modelo criado no exercício de fixação


admin.site.site_header = "Trybe Products E-commerce"
admin.site.register(Product)
admin.site.register(Customer)
