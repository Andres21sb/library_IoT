'''
autor: Andrés Méndez Solano
fecha: 2020-04-22
    
        Este script se encarga de levantar un servidor web con Flask y de definir las rutas para recibir los datos de dispositivos IoT
'''

# app.py
from flask import Flask, request
from database import insert_data,register_publisher,register_subscriber

app = Flask(__name__)

# Ruta para recibir datos de los dispositivos IoT
@app.route('/publishers', methods=['POST'])
def envio_datos():
    data = request.get_json()
    print('Datos recibidos -> ', data)
    publisher_name = data['publisher_name']
    timestamp = data['data'].pop('timestamp', None)
    save_to_db = data['save_to_db']
    if save_to_db:
        try:
            # registrar publisher
            register_publisher(publisher_name)
            for key, value in data['data'].items():
                attribute_data = {
                    'publisher_name': publisher_name,
                    'attribute_name': key,
                    'attribute_value': value,
                    'timestamp': timestamp
                }
            
                insert_data(attribute_data)
        except Exception as e:
            print('Error -> ', e)
            return 'Error saving in db', 500

    return 'Datos recibidos', 200

# Ruta para registrar los subscriptores
@app.route('/subscribers', methods=['POST'])
def register_subscriber():
    data = request.get_json()
    print('Datos recibidos -> ', data)
    # Extraer nombre del subscriptor
    subscriber_name = data['subscriber_name']
    # Extraer array de topics (publisher names)
    topic = data['topic']
    save_to_db = data['save_to_db']
    if save_to_db:
        try:
            # registrar subscriber
            register_subscriber(subscriber_name, topic)
        except Exception as e:
            print('Error -> ', e)
            return 'Error saving subscriber in db', 500

    return 'Datos recibidos', 200

if __name__ == '__main__':
    app.run(debug=True)