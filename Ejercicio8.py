""" Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011
en el campus Vitacura.
Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una """
def pagoProducto(precio,tipoProducto):
    print("Solo se aceptan de $10, $50 y $100.")
    pago = int(input("Ingrese la moneda:"));
    totalPagado=pago
    while precio > totalPagado:
          pago = int(input("Ingrese otra moneda:"));
          totalPagado += pago;
    vuelto(precio,totalPagado,tipoProducto)

def vuelto(precio,totalPagado,tipoProducto):
    print("Vuelto de la compra del Producto",tipoProducto);
    resto= -1;
    if totalPagado > precio :
        resto = totalPagado - precio;
        while resto !=0:
            if resto >= 100:
                print("Vuelto de $100");
                resto-=100;
            elif resto >= 50:
                print("Vuelto de $50");
                resto-=50;
            else:
                print("Vuelto de $10");
                resto-= 10;


def productoA():
    print("El producto cuesta $270");
    pagoProducto(270,"A");

def productoB():
    print("El producto cuesta $340");
    pagoProducto(340,"B");

def productoC():
    print("El producto cuesta $390");
    pagoProducto(390,"C");



print("**************SUPER VENTAS**************");
print("Productos en venta de tipo A B y C.")
producto = input("Ingrese el tipo de Producto que desea comprar:");
if producto == "A" or producto == "a" :
    productoA();
elif producto == "B" or producto == "b":
    productoB();
elif producto == "C" or producto == "c":
     productoC();
else:
    print("El tipo de producto ingresado no es válido.")




