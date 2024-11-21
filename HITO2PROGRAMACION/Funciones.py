import BD

cursor = BD.conexion.cursor()

# Funcion para realizar y guardar reguistro eh informacion del cliente
def registro_cliente():
    nombre = input("Ingrese nombre de cliente\n")
    direccion = input("Ingrese direccion de cliente\n")
    telefono = input("Ingrese numero de telefono del cliente\n")
    correo = input("Ingrese correo electronico del cliente\n")

    cursor.execute("INSERT INTO cliente (idcliente, nombre, direccion, telefono, correo) VALUES (NULL,%s, %s, %s, %s);", (nombre, direccion, telefono, correo))
    BD.conexion.commit()

    print("Se a ingresado el cliente con exito")

# Funcion para visualizar todos los usuarios registrados
def visualizar_cliente():
    cursor.execute("SELECT * FROM tiendaonline.cliente;")
    registros = cursor.fetchall()
    for cliente in registros:
        print(f"ID Cliente: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Teléfono: {cliente[3]}, Correo: {cliente[4]}")

# Funcion para realizar busqueda de clientes por su idcliente
def busqueda_cliente():
    idcliente = int(input("Ingrese numero de idusuario: "))
    cursor.execute("SELECT * FROM tiendaonline.cliente where idcliente = %s;", (idcliente,))
    cliente = cursor.fetchall()
    print(f'{cliente}\n')

# Funcion para realizar una compra mostrando lista de productos y mostrando los usuarios para selecionar usuario con el que estamos operando para realizar la compra
def compra_productos():
    visualizar_cliente()
    cursor.execute("SELECT * FROM tiendaonline.productos;")
    productos = cursor.fetchall()
    print("---Lista de productos---")
    for compra in productos:
       print(f"ID Producto: {compra[0]}, Nombre: {compra[1]}, Precio: {compra[2]}, Cantidad: {compra[3]}")
    
    idcliente = int(input("Ingrese tu idcliente : "))
    idproducto = int(input("Ingrese el id del producto que quieras comprar : "))
    cantidad = int(input("Ingrese la cantidad de productos que desea comprar : "))
    cursor.execute("INSERT INTO compras_cliente (idcompra, idcliente, idproducto, cantidad) VALUES (NULL, %s, %s, %s);", (idcliente, idproducto, cantidad))
    BD.conexion.commit()
    print("Ha realizado correctamente su compra.")
    
# Funcion para realizar un seguimiento del pedido mediante el idpedido
def seguimiento_pedido():
    print("Esta dentro del Sistema de Seguimiento de productos\n")
    print("¿Cual es su pedido?")
    cursor.execute("SELECT * FROM compras_cliente ORDER BY idcliente = LAST_INSERT_ID();")
    compra_usuario = cursor.fetchall()
    for pedido in compra_usuario:
       print(f"ID Pedido: {pedido[0]}, ID Usuario: {pedido[1]}, ID Producto: {pedido[2]}, Cantidad Comprada: {pedido[3]}")

    idcompra = int(input("Ingrese el número de pedido que quiera seguir :"))
    consulta = """
    SELECT 
        cliente.*, 
        productos.*, 
        compras_cliente.idcompra, 
        compras_cliente.cantidad AS cantidad_comprada,
        (compras_cliente.cantidad * productos.precio) AS total_por_producto
    FROM 
        compras_cliente
    JOIN 
        cliente ON compras_cliente.idcliente = cliente.idcliente
    JOIN 
        productos ON compras_cliente.idproducto = productos.idproducto
    WHERE 
        compras_cliente.idcompra = %s;
    """
    cursor.execute(consulta, (idcompra,))
    resultados = cursor.fetchall()


    for cliente in resultados:
        print()
        print("---Detalles cliente---\n")
        print(f"IDCliente : {cliente[0]}")
        print(f"Nombre cliente : {cliente[1]}")
        print(f"Dirección : {cliente[2]}")
        print(f"Teléfono : {cliente[3]}")
        print(f"Correo : {cliente[4]}\n")
 
    for compra_cliente in resultados:
        print("---Detalles de la Compra---\n")
        print(f"ID Compra: {compra_cliente[9]}")
        print(f"Cantidad Comprada: {compra_cliente[10]}\n")
   
    for productos in resultados:
        print("---Detalles del Producto---\n")
        print(f"ID Producto: {productos[5]}")
        print(f"Producto: {productos[6]}")
        print(f"Precio Unitario: {productos[8]}\n")