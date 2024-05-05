'''
autor: Andrés Méndez Solano
fecha: 2020-05-04

    Este script simula ser una biblioteca que registra publishers y envia sus datos a un API REST
'''
import requests
import time
import threading

# Función que envía los datos al servidor
def send_data(url, output_data):
    try:
        response = requests.post(url, json=output_data)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print('Excepcion -> ', e)

# Función que registra un publisher y envía los datos al servidor
def register_publisher(func, intervalo, url='https://library-iot.onrender.com/publishers',publisher_name='no name'):
    while True:
        # Recolectar los datos
        data = func()
        # Encerrar los datos en un diccionario
        output_data = {'publisher_name':publisher_name,'data': data}
        print('Enviando datos: ', output_data)

        # Crear y empezar un nuevo hilo para enviar los datos
        threading.Thread(target=send_data, args=(url, output_data)).start()

        # Esperar el intervalo especificado antes de la próxima recolección de datos
        time.sleep(intervalo)
