minutosTramoTotal=0;
print("********************************TRAMOS DE VIAJES********************************.")
print("Ingrese 0 para salir de la carga de tramos y finalizar el programa.")
minutoTramo = int(input("Ingrese los minutos del tramo:"));
while minutoTramo!=0:
    minutosTramoTotal+=minutoTramo;
    minutoTramo = int(input("Ingrese otro valor de los minutos del tramo:"));
hora = int(minutosTramoTotal / 60);
minutos = minutosTramoTotal % 60;
print("EL total de tiempo de todos los tramos es de ",hora,":",minutos,"Hs");


