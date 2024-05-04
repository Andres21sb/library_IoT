'''
autor: Andrés Méndez Solano
fecha: 2020-04-24

    Este script se encarga de la lectura de los datos del termostato y de enviarlos al servidor
'''
import threading
import random
from library.iot_library import register_publisher

# Definir intervalo de tiempo que espera el termostato para volver a hacer la lectura y enviar los datos
intervalo = 5

# Funcion para simular la lectura de la temperatura
def leer_temperatura():
    # Simular lectura dentro de un rango especifico
    temperatura = round(random.uniform(15, 30), 2)
    # random.uniform(15, 30) genera un número aleatorio entre 15 y 30
    # round(numero, 2) redondea el número a dos decimales
    return {'temperatura': temperatura}

# URL del servidor
url = 'https://library-iot.onrender.com/envio-datos'

# Crear y empezar un hilo para el termostato
hilo = threading.Thread(target=register_publisher, args=(leer_temperatura, intervalo, url))
hilo.start()