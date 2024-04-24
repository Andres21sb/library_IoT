'''
autor: Andrés Méndez Solano
fecha: 2020-04-24

    Este script se encarga de la lectura de los datos del smartwatch y de enviarlos al servidor
'''
import requests
import time
import random
from concurrent.futures import ThreadPoolExecutor

#Definir intervalo de tiempo que espera el smartwatch para volver a hacer la lectura y enviar los datos
intervalo = 5

#Funcion para simular la lectura de la frequencia cardiaca
def leer_frecuencia():
    #Simular lectura dentro de un rango especifico
    frecuencia = random.randint(60, 190)
    #random.randint(60, 100) genera un número aleatorio entre 60 y 100
    return frecuencia

#Funcion para enviar datos por http
def enviar_datos(frecuencia):
    #URL del servidor
    url = 'https://library-iot.onrender.com/frecuencia'
    #Datos a enviar
    datos={'frecuencia': frecuencia}
    #intentar enviar los datos
    try:
        #Enviar petición POST al servidor
        response = requests.post(url, data=datos)
        #impresión de respuesta
        print(response.text)
    except requests.exceptions.RequestException as e:
        #En caso de error al enviar los datos
        print('Excepcion -> ',e)

#El loop principal del smartwatch se va a ejecutar indefinidamente
while True:
    #Leer la frecuencia cardiaca del smartwatch
    frecuencia = leer_frecuencia()
    print('Frecuencia actual: ', frecuencia)
    
    # Crear un ThreadPoolExecutor para ejecutar la función enviar_datos en un hilo separado
    with ThreadPoolExecutor() as executor:
        # Ejecutar la función enviar_datos con la frecuencia como argumento
        executor.submit(enviar_datos, frecuencia)
    
    #Esperar un tiempo antes de volver a leer la frecuencia cardiaca
    time.sleep(intervalo)