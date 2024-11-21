import Funciones as fc
import menu as nm

# Hacemos una funcion para que nos realice todas las funciones del archivo Funciones para utilizarlas de la manera y orden que queramos
def funcion_menu(menu):
    while True:
        nm.mostrar_menu()
        menu = int (input("Seleccione una opcion:  \n"))
        if menu == 1 :
                fc.registro_cliente()
        
        if menu == 2:
                print("\n\n---SELECCIONE---")
                print("\n1. Visualizar Cliente")
                print("2. Busqueda de cliente\n")
                menu2 = int (input("Seleccione una opcion:  \n"))
                
                if menu2 == 1 :
                        fc.visualizar_cliente()
                if menu2 == 2 :
                        fc.busqueda_cliente()
        if menu == 3:
        
                fc.compra_productos()
            
        if menu == 4:
                fc.seguimiento_pedido()

        if menu == 5:
                
            print("Ha salido correctamente del programa")
            break