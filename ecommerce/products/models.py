# ecommerce/products/models.py

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
      upload_to="media/products", null=True, blank=True
    )

    def __str__(self):
        return f'{self.name} - {self.price}'


# Primeiro passo: crie uma classe que represente um modelo para
# a tabela Customers, dentro do arquivo ecommerce/products/models.py:
class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)


# Segundo passo: crie a migration:
# python3 manage.py makemigrations


# Terceiro passo: execute a migration:
# python3 manage.py migrate


# Exercicio 2
# Para adicionar os dados usando o terminal do Django:

# Primeiro passo: entre no terminal com o comando:
# python3 manage.py shell

# Segundo passo: importe o modelo criado para a tabela customers:
# from products.models import Customer

# Terceiro passo: crie o primeiro objeto solicitado e salve-o
# no banco de dados:
# saul = Customer(name="Saul Goodman",
#           address="Rua das Flores, 123", phone="(85) 99998-9999")
# saul.save()

# Quarto passo: crie o segundo objeto solicitado e
# salve-o no banco de dados:
# mike = Customer(name="Mike Ehrmantraut",
#           address="Quadra 54, casa 66", phone="(21) 99988-8888")
# mike.save()

# Quinto passo: crie o terceiro objeto solicitado e salve-o no banco de dados:
# kim = Customer(name="Kim Wexler",
#           address="Rua Mesa Verde, 5", phone="(51) 99977-7979")
# kim.save()
