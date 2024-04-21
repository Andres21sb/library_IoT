from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Endpoints

#test
@app.route('/test')
def test():
    return 'Test from flask API'
