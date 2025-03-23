# Requests

import requests

# Programa

nombre = 'José'

json = {
    'nombre': 'Pablito'
}

url = f'http://127.0.0.1:5000/return_nombre/{nombre}'
res = requests.get(url, json=json)

print(res)
