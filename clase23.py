from flask import Flask, request
import pymysql


app = Flask(__name__)

def get_db_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='empleados_reloj_pruebas',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

@app.route('/')
def home():
    return 'Hola mundo'

@app.route('/empleados')
def empleados():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM empleados ORDER BY apellido ASC')
    data = cursor.fetchall()
    print(data)
    conn.close()
    return data

@app.route('/insertar_empleado', methods=['POST'])
def insertar_empleado():
    conn = get_db_connection()
    cursor = conn.cursor()
    empleado = request.get_json()
    query = f"""
    INSERT INTO empleados (nombre, apellido, legajo, funcion, horario_fk) 
    VALUES 
    (\"{empleado['nombre']}\", \"{empleado['apellido']}\", \"{empleado['legajo']}\", 
    \"{empleado['funcion']}\", \"{empleado['horario_fk']}\")
    """
    cursor.execute(query)
    conn.commit()
    conn.close()
    return 'Empleado añadido con éxito'


if __name__ == '__main__':
    app.run(debug=True)