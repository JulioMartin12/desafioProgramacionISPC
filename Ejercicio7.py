""" La secuencia de Collatz de un número entero se construye de la siguiente forma:
● si el número es par, se lo divide por dos;
● si es impar, se le multiplica tres y se le suma uno;
La sucesión termina al llegar a uno.
Desarrolle un programa que entregue la secuencia de Collatz de un número entero: """
numero = int(input("Ingrese un número entero:"));
resultado = str(numero) + " ";
while numero != 1:
    if numero % 2 == 0:
        numero = int(numero/2);
        resultado+=(str(numero) + " ");
    else:
        numero= (numero * 3) + 1;
        resultado+=(str(numero) + " ");
print(resultado);

        
