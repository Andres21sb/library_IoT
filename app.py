'''
autor: Andrés Méndez Solano
fecha: 2020-04-22
    
        Este script se encarga de levantar un servidor web con Flask y de definir las rutas para recibir los datos de dispositivos IoT
'''

from flask import Flask, request
app = Flask(__name__)

# Endpoints

#test
@app.route('/test')
def test():
    return 'Test from flask API'


# Ruta para manejar el post de los datos de los dispositivos publishers IoT
@app.route('/publishers', methods=['POST'])
def envio_datos():
    data = request.get_json()
    for key, value in data.items():
        print(f'{key}: {value}')
    return 'Datos recibidos', 200



if __name__ == '__main__':
    app.run(debug=True)