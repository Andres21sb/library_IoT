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
    return 'Hello, World! from Mongo-suscriber'

# Ruta para recibir datos de los dispositivos IoT
@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    print('Datos recibidos -> ', data)
    return 'Datos recibidos', 200




if __name__ == '__main__':
    # registrar un subscriber
    register_subscriber('Mongo-suscriber',['electricidad_v1'], 'https://mongo-suscriber.onrender.com/data')
    app.run(debug=True)