""" Anagrama. Escribe una función que reciba dos palabras y retorne
verdadero o falso según sean o no anagramas.
● Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
otra palabra inicial.
● NO hace falta comprobar que ambas palabras existen.
● Dos palabras exactamente iguales no son anagrama. """
def verificarAnagrama(palabra1, palabra2):
    palabraAuxiliar = list(palabra2);
    for i in palabra1:
        palabraAuxiliar.remove(i);
    return len(palabraAuxiliar);  
   
palabra1=input("Ingrese la primera palabra:");
palabra2=input("Ingrese la segunda palabra:");
if len(palabra1) != len(palabra2):
    print("Las palabras",palabra1, " y ",palabra2," no tienen la misma cantidad de letras por ende no son ANAGRAMA");
elif verificarAnagrama(palabra1,palabra2) == 0:
     print("Las palabras",palabra1, " y ",palabra2," son ANAGRAMA");
else:
    print("Las palabras",palabra1, " y ",palabra2," no son ANAGRAMA");
    