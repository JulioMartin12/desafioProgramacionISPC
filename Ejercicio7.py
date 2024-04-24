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

        
