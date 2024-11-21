DROP DATABASE IF EXISTS tiendaonline;
CREATE DATABASE tiendaonline;
USE tiendaonline;
 
CREATE TABLE cliente (
    idcliente INT auto_increment PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    direccion VARCHAR(35) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    correo VARCHAR(30) UNIQUE NOT NULL
);
 
CREATE TABLE productos (
    idproducto INT auto_increment PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    precio FLOAT(10) NOT NULL,
    cantidad INT NOT NULL
);
 
CREATE TABLE compras_cliente (
    idcompra INT auto_increment PRIMARY KEY,
    idcliente INT,
    idproducto INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (idcliente) REFERENCES cliente(idcliente),
    FOREIGN KEY (idproducto) REFERENCES productos(idproducto)
);

INSERT INTO productos (nombre, precio, cantidad) VALUES ('Laptop', 1500.00, 25);
INSERT INTO productos (nombre, precio, cantidad) VALUES ('Smartphone', 800.00, 50);
INSERT INTO productos (nombre, precio, cantidad) VALUES ('Tablet', 600.00, 30);
INSERT INTO productos (nombre, precio, cantidad) VALUES ('Monitor', 200.00, 40);
INSERT INTO productos (nombre, precio, cantidad) VALUES ('Teclado', 50.00, 100);
INSERT INTO productos (nombre, precio, cantidad) VALUES ('Ratón', 30.00, 120);
INSERT INTO productos (nombre, precio, cantidad) VALUES ('Auriculares', 120.00, 60);
INSERT INTO productos (nombre, precio, cantidad) VALUES ('Cámara', 400.00, 20);
INSERT INTO productos (nombre, precio, cantidad) VALUES ('Impresora', 150.00, 35);
INSERT INTO productos (nombre, precio, cantidad) VALUES ('Disco Duro', 90.00, 75);

 
