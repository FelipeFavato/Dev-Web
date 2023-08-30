# Baseando-se em uma página contendo detalhes sobre um livro
# (http://books.toscrape.com/catalogue/the-grand-design_405/index.html),
# faça a extração dos campos título, preço, descrição e url
# contendo a imagem de capa do livro.

# ⚠️ O preço deve vir somente valores numéricos e ponto. Ex: Â£13.76 -> 13.76.
# ⚠️ A descrição deve ter o sufixo “more…” removido quando existir.
# ⚠️ Os campos extraídos devem ser apresentados separados por vírgula.
# Ex: título,preço,descrição,capa.

import requests
import parsel

# Encontrar o padrão da URL e fazer uma URL_BASE
URL_BASE = "http://books.toscrape.com/catalogue/"
# Faz o request com o metodo get(url_total)
response = requests.get(URL_BASE + "the-grand-design_405/index.html")
# Armazena na variavel selector a classe Selector vinda do Parsel
selector = parsel.Selector(response.text)

# Armazena na variavel title o texto da tag H1
title = selector.css("h1::text").get()

# selector.css(.classe) => Função para pegar pelo seletor CSS
# classe = product_main ---> .product_main
# '>' => Inidica que vou pegar algo que esta dentro dela
# classe = price_color --> .price_color
# '::' => Indica que vou pegar algo da classe
# text => Nesse caso, o texto da classe
# re_first(r"") => expressão regular para capturar algo especifico
price = selector.css(
    ".product_main > .price_color::text").re_first(r"\d*\.\d{2}")

# id = product_description ---> #product_description
# '~' => Indica que vai pegar a proxima tagHtml (irmã)
description = selector.css("#product_description ~ p::text").get()
suffix = "...more"
if description.endswith(suffix):
    # Vai pegar tudo antes do suffix que esta sendo passado
    description = description[:-len(suffix)]

cover = URL_BASE + selector.css("#product_gallery img::attr(src)").get()

availability = selector.css(
    '.product_main .availability::text').re_first(r'\d')

print(title, price, description, cover, availability, sep=",")
