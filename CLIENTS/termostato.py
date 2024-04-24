'''
autor: Andrés Méndez Solano
fecha: 2020-04-24

    Este script se encarga de la lectura de los datos del termostato y de enviarlos al servidor
'''
import requests
import time
import random

#Definir intervalo de tiempo que espera el termostato para volver a hacer la lectura y enviar los datos
intervalo = 5

#Funcion para simular la lectura de la temperatura
def leer_temperatura():
    #Simular lectura dentro de un rango especifico
    temperatura = round(random.uniform(15, 30), 2)
    #random.uniform(15, 30) genera un número aleatorio entre 15 y 30
    #round(numero, 2) redondea el número a dos decimales
    return temperatura

#Funcion para enviar datos por http
def enviar_datos(temperatura):
    #URL del servidor
    url = 'https://library-iot.onrender.com/temperatura'
    #Datos a enviar
    datos={'temperatura': temperatura}
    #intentar enviar los datos
    try:
        #Enviar petición POST al servidor
        response = requests.post(url, data=datos)
        #impresión de respuesta
        print(response.text)
    except requests.exceptions.RequestException as e:
        #En caso de error al enviar los datos
        print('Excepcion -> ',e)
        


#El loop principal del termostato se va a ejecutar indefinidamente
while True:
    #Leer la temperatura del termostato
    temperatura = leer_temperatura()
    print('Temperatura actual: ', temperatura)
    
    #enviar datos por http
    enviar_datos(temperatura)
    
    #Esperar un tiempo antes de volver a leer la temperatura
    time.sleep(intervalo)
