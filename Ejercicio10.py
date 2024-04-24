def torreTomaAlfil(tablero, filaTorre,columnaTorre):
      for fila in range(len(tablero)):
             if 'A' in tablero[fila] and ((int(filaTorre)) -1) == fila:
                   print("esta en la misma fila:", fila + 1)
                   print("Torre toma alfil con movimiento horizontal en la fila:", fila+1)
                   break;
             else:
                   for columna in range(len(tablero[fila])):
                        if tablero[fila][columna] == 'A' and ((int(columnaTorre)) -1) == columna:
                         print("esta en la misma columna:", columna + 1); 
                         print("Torre toma alfil con movimiento vertical en la columna:", columna+1)
                         break;
      print("La torre no puede tomar el alfil, con ningún movimiento , horizontal o vertical");
                
def alfilTomaTorre(tablero, filaAlfil, columnaAlfil):
    
     if diagonalPrincipal(tablero, filaAlfil, columnaAlfil):
           print("El alfil toma torre con movimiento diagonal");
     elif diagonalSecundaria(tablero, filaAlfil, columnaAlfil):
           print("El alfil toma torre con movimiento diagonal");
     else:
           print("El alfil no puede toma torre con ningún movimiento diagonal");


def diagonalPrincipal(tablero, filaAlfil, columnaAlfil):
      flag=False;
      for fila in range(len(tablero)):
           if flag:
              break;
           for columna in range(len(tablero[fila])):
                 if (int(filaAlfil - columnaAlfil)) == 0 and ((fila+1) - (columna+1))==0 and tablero[fila][columna]=='T':
                       flag=True;
                       break;
                 elif (int(filaAlfil + columnaAlfil)) % 2 != 0 and ((fila+1) + (columna+1)) % 2 != 0 and tablero[fila][columna]=='T':
                       flag=True;
                       break;
      return flag;  
  
def diagonalSecundaria(tablero, filaAlfil, columnaAlfil):
      flag=False;
      for fila in range(len(tablero)):
           if flag:
              break;
           for columna in range(len(tablero[fila])):
                 if (int(filaAlfil + columnaAlfil)) == ((fila+1) + (columna+1)) and tablero[fila][columna]=='T':
                       flag=True;
                       break;
      return flag;             
         

tablero = [[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
print("*************TABLERO DE AJEDREZ*************")
for fila in tablero:
       print("|", " ".join(map(str,fila)) ,"|");
print("******Ingrese la posición de la del Alfil******");
alfilFila = (input("Ingrese la posición de la fila del Alfil:"));
alfilColumna = (input("Ingrese la posición de la Columna del Alfil:"));
print("******Ingrese la posición de la Torre******");
torreFila = input("Ingrese la posición de la fila de la Torre:");
torreColumna = input("Ingrese la posición de la Columna de ls Torre:");
tablero[(int(alfilFila))-1][(int(alfilColumna))-1]="A";
tablero[(int(torreFila))-1][(int(torreColumna))-1]="T";
print("*************TABLERO DE AJEDREZ*************")
print("*********Con las piezas posicionadas********")
for fila in tablero:
       print("|", " ".join(map(str,fila)) ,"|");

torreTomaAlfil(tablero,torreFila,torreColumna);
alfilTomaTorre(tablero,(int(alfilFila)),(int(alfilColumna)));


  