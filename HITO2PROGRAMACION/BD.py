# Importamos la base de datos
import mysql.connector

#Hacemos la conexion en la base de datos en la que guardaremos nuestros datos ingresados
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="curso",
    database="tiendaonline"
)

# Hacemos una funcion para que si la conexion con la base de datos es correcta nos lo diga
def conexion_BD():

    if conexion.is_connected():
        print("Conexión exitosa a la base de datos")