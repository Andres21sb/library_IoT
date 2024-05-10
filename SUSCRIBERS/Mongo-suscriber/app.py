'''
autor: Andrés Méndez Solano
fecha: 2020-05-08
    
        Este script se encarga de levantar un servidor web con Flask y de guardar los datos que recibe en una base de datos de MongoDB
'''

# app.py
from flask import Flask, request
from library.iot_library import register_subscriber


app = Flask(__name__)
#hello world
@app.route('/')
def hello_world():
        # registrar un subscriber
    print('Registrando subscriber')
    try:
        req = register_subscriber('Mongo-suscriber',['electricidad_v1'], 'https://mongo-suscriber.onrender.com/data')
        print('Respuesta del servidor -> ', req)
        print('Subscriber registrado')
    except Exception as e:
        print('Error registrando subscriber -> ', e)
        return 'Error registrando subscriber', 500
    return 'Hello, World! from Mongo-suscriber'

# Ruta para recibir datos de los dispositivos IoT
@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    print('Datos recibidos -> ', data)
    return 'Datos recibidos', 200




if __name__ == '__main__':
    app.run(debug=True)