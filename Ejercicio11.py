""" Piedra, papel y tijera. En cada ronda del juego del cachipún, los dos competidores
deben elegir entre jugar tijera, papel o piedra.
Las reglas para decidir quién gana la ronda son: tijera le gana a papel, papel le gana a
piedra, piedra le gana a tijera, y todas las demás combinaciones son empates.
El ganador del juego es el primero que gane tres rondas.
Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el
marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres
rondas. Los jugadores deben indicar su jugada escribiendo tijera, papel o piedra """

def ganadorJuego(victoriasJugadorA, victoriasJugadorB):
    if victoriasJugadorA == 3:
        print("Ganó el Juego el Jugador A!!!!!");
        print(victoriasJugadorA, " - ", victoriasJugadorB);
        return True;
    elif victoriasJugadorB == 3:
        print("Ganó el juego el Jugador B!!!!!");
        print(victoriasJugadorA, " - ", victoriasJugadorB);
        return True;
    return False;

def mensajeVictoria(jugadas,jugadaJugadorA,jugadaJugadorB,victoriasJugadorA,victoriasJugadorB, ganador):
        print("Jugador A:",jugadas[jugadaJugadorA]);
        print("Jugador B:",jugadas[jugadaJugadorB]);
        print("Victoria del Jugador !!!",ganador);
        print("Resultado de la Partida:",victoriasJugadorA," - ", victoriasJugadorB);

def controlCadaPartida(jugadas,jugadaA,jugadaB):
    global victoriasJugadorA, victoriasJugadorB;
    if   jugadas[jugadaA] == "Piedra":
         if jugadas[jugadaB] == "Tijera":
              victoriasJugadorA += 1;
              mensajeVictoria(jugadas,jugadaA,jugadaB,victoriasJugadorA,victoriasJugadorB, "A")
         else:
              victoriasJugadorB += 1;
              mensajeVictoria(jugadas,jugadaA,jugadaB,victoriasJugadorA,victoriasJugadorB, "B")
    elif  jugadas[jugadaA] == "Papel":
        if jugadas[jugadaB] == "Piedra":
              victoriasJugadorA += 1;
              mensajeVictoria(jugadas,jugadaA,jugadaB,victoriasJugadorA,victoriasJugadorB, "A")
        else:
              victoriasJugadorB += 1;
              mensajeVictoria(jugadas,jugadaA,jugadaB,victoriasJugadorA,victoriasJugadorB, "B")
    elif  jugadas[jugadaA] == "Tijera":
        if jugadas[jugadaB] == "Papel":
              victoriasJugadorA += 1;
              mensajeVictoria(jugadas,jugadaA,jugadaB,victoriasJugadorA,victoriasJugadorB, "A")
        else:
              victoriasJugadorB += 1;
              mensajeVictoria(jugadas,jugadaA,jugadaB,victoriasJugadorA,victoriasJugadorB, "B");

print("**************************JUEGO DE PIEDRA, PAPEL Y TIJERA**************************");
print("El juego termina cuando un jugador gane 3 partidas seguidas");
ganador=False;
victoriasJugadorA = 0;
victoriasJugadorB = 0;
jugadas=["Piedra", "Papel", "Tijera"];
while ganador!= True:
    print("Seleccione una jugada.");
    print("0)Piedra.")
    print("1)Papel.")
    print("2)Tijera.")
    jugadaJugadorA=int(input("Ingrese la jugada del Jugador A:"));
    jugadaJugadorB=int(input("Ingrese la jugada del Jugador B:"));
    if jugadaJugadorA == jugadaJugadorB:
        print("Jugador A:",jugadas[jugadaJugadorA]);
        print("Jugador B:",jugadas[jugadaJugadorB]);
        print("Empate!!!");
        print("Resultado de la Partida:",victoriasJugadorA," - ", victoriasJugadorB);
    else:
         controlCadaPartida(jugadas,jugadaJugadorA,jugadaJugadorB);
    ganador=ganadorJuego(victoriasJugadorA,victoriasJugadorB);
  
     
