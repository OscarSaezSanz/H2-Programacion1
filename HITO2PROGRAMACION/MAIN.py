# Importamos los archivos que tenemos en la carpeta para que puedan actuar en este archivo
import BD
import funciones_Menu as fm

# Llamamos a las funciones de otros archivos para que se muestren en este complementandose 
BD.conexion_BD()
fm.funcion_menu('menu')
