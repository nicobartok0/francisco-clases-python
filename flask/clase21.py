from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    json = {
        'Nombre': 'Juan',
        'Apellido': 'Pérez'
    }
    return json

@app.route('/hola_mundo')
def hola_mundo():
    return 'Hola mundo'

@app.route('/return_nombre', methods=['GET'])
def return_nombre():
    return 'Alberto'

@app.route('/return_nombre/<nombre>')
def return_nombre_var(nombre):
    return nombre

@app.route('/nombre_json')
def nombre_json():
    data = request.get_json()
    nombre = data['nombre']
    return f'Hola, {nombre}'

if __name__ == '__main__':
    app.run(debug=True)