'''
autor: Andrés Méndez Solano
fecha: 2020-04-24

    Este script se encarga de la lectura de los datos del termostato y de enviarlos al servidor
'''
import threading
import random
from library.iot_library import register_publisher
from datetime import datetime

# Definir intervalo de tiempo que espera el termostato para volver a hacer la lectura y enviar los datos
intervalo = 5

#nombre del publisher
publisher = 'termostato_v1'

# Funcion para simular la lectura de la temperatura
def leer_temperatura():
    # Simular lectura dentro de un rango especifico
    temperatura = round(random.uniform(15, 30), 2)
    # tiempo en el que se hizo la lectura
    timestamp = datetime.now().strftime("%H:%M:%S %Y-%m-%d")
    # random.uniform(15, 30) genera un número aleatorio entre 15 y 30
    # round(numero, 2) redondea el número a dos decimales
    return {'temperatura': temperatura,'timestamp': timestamp}

# URL del servidor
url = 'http://127.0.0.1:5000/envio-datos'

# Crear y empezar un hilo para el termostato
hilo = threading.Thread(target=register_publisher, args=(leer_temperatura, intervalo, url,publisher))
hilo.start()