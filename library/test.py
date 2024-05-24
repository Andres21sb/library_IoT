import unittest
import requests
import time
import threading
import coverage
from library.iot_library import send_data, register_publisher, register_subscriber, send_data_to_subscriber, Notify_subscribers, my_partial_fn
# Inicializar la cobertura
cov = coverage.Coverage()
cov.start()

""" # Funciones de prueba
class TestSendData(unittest.TestCase):
    def test_send_data(self):
        print('Test Send Data')
        url = 'https://library-iot.onrender.com/publishers'
        output_data = {'publisher_name': 'TestPublisher', 'data': 'Test Data', 'save_to_db': True}
        response = requests.post(url, json=output_data)
        self.assertEqual(response.status_code, 200) """

""" class TestRegisterPublisher(unittest.TestCase):
    def test_register_publisher(self):
        def test_data_function():
            return "Test Data"
        
        intervalo = 5
        url = 'https://library-iot.onrender.com/publishers'
        publisher_name = 'TestPublisher'
        save_to_db = True
        register_publisher(test_data_function, intervalo, url, publisher_name, save_to_db)

class TestRegisterSubscriber(unittest.TestCase):
    def test_register_subscriber(self):
        subscriber_name = 'TestSubscriber'
        topics = ['topic1', 'topic2']
        suscriber_endpoint = 'https://mongo-suscriber.onrender.com/data'
        url = 'https://library-iot.onrender.com/subscribers'
        response_text = register_subscriber(subscriber_name, topics, suscriber_endpoint, url)
        self.assertTrue('exitosa' in response_text)

class TestSendDataToSubscriber(unittest.TestCase):
    def test_send_data_to_subscriber(self):
        url = 'https://mock-subscriber.onrender.com/data'
        output_data = {'data': 'Test Data'}
        send_data_to_subscriber(url, output_data)

class TestNotifySubscribers(unittest.TestCase):
    def test_notify_subscribers(self):
        subscribers = [('https://subscriber1.onrender.com',), ('https://subscriber2.onrender.com',)]
        data = 'Test Notification Data'
        Notify_subscribers(subscribers, data) """

# Pruebas de library/iot_library.py
class TestLibrary(unittest.TestCase):
    
    # Prueba de la función send_data que se ejecuta de manera correcta
    def test_send_data(self):
        print('Test Send Data')
        url = 'https://library-iot.onrender.com/publishers'
        output_data = {'publisher_name': 'TestPublisher', 'data': {'frecuencia': 125, 'timestamp': '00:00:28 2024-05-24'}, 'save_to_db': True}
        send_data(url, output_data)
    # Prueba de la funcion send data que levanta una excepcion por url incorrecta
    '''
    Excepcion ->  HTTPSConnectionPool(host='library-iot.onrender.comm', port=443): Max retries exceeded with url: /publishers (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x00000216FF3E2CD0>: Failed to resolve 'library-iot.onrender.comm' ([Errno 11001] getaddrinfo failed)"))
    '''
    def test_send_data_exception(self):
        print('Test Send Data Exception')
        url = 'https://library-iot.onrender.comm/publishers'
        output_data = {'publisher_name': 'TestPublisher', 'data': {'frecuencia': 125, 'timestamp': '00:00:28 2024-05-24'}, 'save_to_db': True}
        send_data(url, output_data)



if __name__ == '__main__':
    cov.stop()
    cov.save()
    cov.html_report()
    unittest.main()