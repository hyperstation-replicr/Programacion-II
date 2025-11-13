import mysql.connector
DB_CONFIG = {
 "host": "localhost",
 "user": "root",
 "password": "",
 "database": "arduino_sensors"
}
def conectar():
 return mysql.connector.connect(**DB_CONFIG)
