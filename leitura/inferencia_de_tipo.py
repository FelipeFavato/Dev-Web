# tipo int é inferido sem que eu precise deixar explícito
var1 = 1

# não faça isso, é verboso e desnecessário
var2: int = 1

# importante deixar explícito que começa como int, mas pode mudar para float
var3: int | float = 1
