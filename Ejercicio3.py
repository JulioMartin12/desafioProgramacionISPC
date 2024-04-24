numero = int(input("Ingrese un número entero:"));
contador=0;
flag = True;
for i in range( 1,numero):
   if contador > 2 :
      print("No es número primo");
      flag=False;
      break;
   if numero % i == 0:
      print( "divisible",i)
      contador+=1;
if flag:
   print("El número ingresado es primo.")
   

   