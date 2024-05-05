'''
autor: Andrés Méndez Solano
fecha: 2020-05-05
    
        Este script se encarga de definir las funciones para la conexión a la base de datos y para insertar los datos en la base de datos
'''
# database.py
import mysql.connector
from mysql.connector import pooling
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

db_config = {
  "user": os.getenv('DB_USER'),
  "password": os.getenv('DB_PASSWORD'),
  "host": os.getenv('DB_HOST'),
  "database": os.getenv('DB_DATABASE'),
  "raise_on_warnings": True
}

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 10,
                                                      **db_config)

def get_connection():
    return cnxpool.get_connection()

def close_connection(cnx):
    cnx.close()

def insert_data(data):
    cnx = get_connection()
    cursor = cnx.cursor()

    add_data = ("INSERT INTO Data "
                "(publisher_name, attribute_name, attribute_value, timestamp) "
                "VALUES (%s, %s, %s, %s)")
    data_data = (data['publisher_name'], data['attribute_name'], str(data['attribute_value']), data['timestamp'])
    cursor.execute(add_data, data_data)

    cnx.commit()
    close_connection(cnx)