import datetime

anio = "29/02/"
anio+=input("Ingrese un año:");
try:
    fecha = datetime.datetime.strptime(anio, "%d/%m/%Y").date()
except ValueError:
    print("No es un Año Bisiesto.")
else:
    print("El año es Bisiesto!")

