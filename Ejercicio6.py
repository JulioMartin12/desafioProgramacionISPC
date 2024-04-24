import random
renglonesTriangulo = int(input("Ingrese la cantidad de renglones del tríangulo Rectángulo:"));
for i in range(1,renglonesTriangulo + 1):
    print(str(random.randint(0,9))*i);