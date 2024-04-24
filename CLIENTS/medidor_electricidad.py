'''
autor: Andrés Méndez Solano
fecha: 2020-04-24

    Este script se encarga de la lectura de los datos del medidor de electricidad y de enviarlos al servidor
'''
import requests
import time
import random

#Definir intervalo de tiempo que espera el medidor para volver a hacer la lectura y enviar los datos
intervalo = 5

#Funcion para simular la lectura de la corriente
def leer_corriente():
    #Simular lectura dentro de un rango especifico
    corriente = round(random.uniform(0, 10), 2)
    #random.uniform(0, 10) genera un número aleatorio entre 0 y 10
    #round(numero, 2) redondea el número a dos decimales
    return corriente

#Funcion para enviar datos por http
def enviar_datos(corriente):
    #URL del servidor
    url = 'https://library-iot.onrender.com/corriente'
    #Datos a enviar
    datos={'corriente': corriente}
    #intentar enviar los datos
    try:
        #Enviar petición POST al servidor
        response = requests.post(url, data=datos)
        #impresión de respuesta
        print(response.text)
    except requests.exceptions.RequestException as e:
        #En caso de error al enviar los datos
        print('Excepcion -> ',e)

#El loop principal del medidor se va a ejecutar indefinidamente
while True:
    #Leer la corriente del medidor
    corriente = leer_corriente()
    print('Corriente actual: ', corriente)
    
    #enviar datos por http
    enviar_datos(corriente)
    
    #Esperar un tiempo antes de volver a leer la corriente
    time.sleep(intervalo)