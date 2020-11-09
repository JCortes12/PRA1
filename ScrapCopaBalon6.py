#Importamos las librerías que vamos a usar, incluyendo la de BeautifulSoup
import requests
import pandas as pd

from bs4 import BeautifulSoup
#Importamos la página web de la que vamos a traer la información
url = 'https://www.encopadebalon.com/es/32-rioja'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

# Como los nombres están en grupos que empiezan con h5, los traemos todos y dentro de ellos buscamos la variable a.product-name
for tag in soup.findAll('h5'):
    nombre = soup.find_all('a', class_='product-name')
    nombres = list()
    for i in nombre:
            nombres.append(i.text)
    print(nombres)

# Buscamos los precios que están en span.price product-price
precio = soup.find_all('span', class_='price product-price')
precios = list()
for i in precio:
        precios.append(i.text)
print(precios)

#creamos el dataset, eliminando duplicados
df = pd.DataFrame(('nombres' ,'precios'), index=list())
df.drop_duplicates()
print(df)

#lo pasamos a un fichero .csv
df.to_csv('PreciosVionoRioja.csv', index=False)