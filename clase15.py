from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return "Esta es la ruta base"

# Ruta con un parámetro dinámico
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"¡Hola, {nombre.capitalize()}!"

# Ruta para otra página
@app.route('/about')
def acerca():
    return "Aquí se devolverán otros datos"

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
