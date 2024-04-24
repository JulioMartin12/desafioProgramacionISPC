""" Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
entero de horas h, que indique qué hora marcará el reloj dentro de h horas: """

horaActualT= int(input("Ingrese la hora actual en formato de 24hs:"));
cantidadHorasH= int(input("Ingrese cantidad de horas:"));
horaFinal=(horaActualT + cantidadHorasH) % 24
print("En", cantidadHorasH, "horas, el reloj marcara las", horaFinal);
