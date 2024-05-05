'''
autor: Andrés Méndez Solano
fecha: 2020-04-24

    Este script se encarga de la lectura de los datos del smartwatch y de enviarlos al servidor
'''
import threading
import random
from library.iot_library import register_publisher
from datetime import datetime

#nombre del publisher
publisher = 'smartwatch_v1'

# Definir intervalo de tiempo que espera el termostato para volver a hacer la lectura y enviar los datos
intervalo = 5

#Funcion para simular la lectura de la frequencia cardiaca
def leer_frecuencia():
    #Simular lectura dentro de un rango especifico
    frecuencia = random.randint(60, 190)
    # tiempo en el que se hizo la lectura
    timestamp = datetime.now().strftime("%H:%M:%S %Y-%m-%d")
    #random.randint(60, 100) genera un número aleatorio entre 60 y 100
    return {'frecuencia': frecuencia,'timestamp': timestamp}

# URL del servidor
#url = 'http://127.0.0.1:5000/publishers'
url = 'https://library-iot.onrender.com/publishers'

# Crear y empezar un hilo para el termostato
hilo = threading.Thread(target=register_publisher, args=(leer_frecuencia, intervalo, url,publisher))
hilo.start()