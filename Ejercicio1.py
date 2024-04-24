""" Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
número con los dígitos en orden inverso: """

numero3Digitos= input("Ingrese un entero de 3 dígitos:");
if len(numero3Digitos) == 3 and numero3Digitos.isdigit():
   reverso = reversed(numero3Digitos);
   print( "".join(list(reverso)));
else:
   print("El valor ingresado no es valido.");