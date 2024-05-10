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
def register_publisher(func, intervalo, url='https://library-iot.onrender.com/publishers',publisher_name='no name',save_to_db=False):
    while True:
        # Recolectar los datos
        data = func()
        # Encerrar los datos en un diccionario
        output_data = {
            'publisher_name':publisher_name,
            'data': data,
            'save_to_db': save_to_db}
        print('Enviando datos: ', output_data)

        # Crear y empezar un nuevo hilo para enviar los datos
        threading.Thread(target=send_data, args=(url, output_data)).start()

        # Esperar el intervalo especificado antes de la próxima recolección de datos
        time.sleep(intervalo)

# Función que registra un subscriber
def register_subscriber(subscriber_name,topics=[],suscriber_endpoint='https://mongo-suscriber.onrender.com/data', url='https://library-iot.onrender.com/subscribers'):
    # Encerrar los nombres de los publicadores en un diccionario
    data = {'subscriber_name': subscriber_name,
            'topics': topics,
            'suscriber_endpoint': suscriber_endpoint}
    print('Solicitando suscripción: ', data)

    # Enviar la solicitud de suscripción al servidor
    response = requests.post(url, json=data)

    # Verificar la respuesta del servidor
    if response.status_code == 200:
        print('Suscripción exitosa')
    else:
        print('Error en la suscripción: ', response.text)
    return response.text
