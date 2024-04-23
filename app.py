from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Endpoints

#test
@app.route('/test')
def test():
    return 'Test from flask API'


# Ruta para manejar la petición de EnvioDatos
@app.route('/envio-datos', methods=['POST'])
def envio_datos():
    # Recuperar los datos enviados en la petición POST
    idlog = request.form['idlog']
    tr = request.form['tr']
    ta = request.form['ta']
    tc = request.form['tc']
    tb = request.form['tb']
    tv = request.form['tv']
    hr = request.form['hr']
    ha = request.form['ha']
    hc = request.form['hc']
    hb = request.form['hb']
    hv = request.form['hv']
    ca = request.form['ca']
    ne = request.form['ne']
    le = request.form['le']
    uv = request.form['uv']
    # Add to dictionary to print
    data = {
        'idlog': idlog,
        'tr': tr,
        'ta': ta,
        'tc': tc,
        'tb': tb,
        'tv': tv,
        'hr': hr,
        'ha': ha,
        'hc': hc,
        'hb': hb,
        'hv': hv,
        'ca': ca,
        'ne': ne,
        'le': le,
        'uv': uv
    }
    print('Datos recibidos: ', data)
    # return 200 and message Datos recibidos
    return 'Datos recibidos'


# Ruta para manejar la petición de EnvioLog
@app.route('/envio-log', methods=['POST'])
def envio_log():
    # Recuperar los datos enviados en la petición POST
    idlog = request.form['idlog']
    description = request.form['description']
    
    print('Datos de log recibidos: ', idlog, description)
    
    # Devolver una respuesta, por ejemplo un mensaje de éxito
    return 'Datos de log recibidos correctamente'

if __name__ == '__main__':
    app.run(debug=True)