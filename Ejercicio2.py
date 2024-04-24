horaActualT= int(input("Ingrese la hora actual en formato de 24hs:"));
cantidadHorasH= int(input("Ingrese cantidad de horas:"));
horaFinal=(horaActualT + cantidadHorasH) % 24
print("En", cantidadHorasH, "horas, el reloj marcara las", horaFinal);
