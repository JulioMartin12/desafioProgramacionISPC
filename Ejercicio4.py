""" Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
tiene la duración en minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0. """

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


