# Faça uma requisição ao recurso usuários da API do Github
# (https://api.github.com/users)
# , exibindo o username e url de todos os usuários retornados.

import requests

response = requests.get("https://api.github.com/users")
json = response.json()

for user in json:
    print(f"{user['login']} {user['url']}")
