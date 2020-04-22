import random 
from string import Template
import os

def PiedraPapelTijera(jugador1, jugador2):

    return solucionesJ1 [jugador1][jugador2] 

solucionesJ1= {
    "piedra":{
        "piedra": "empate",
        "papel":"pierde",
        "tijera":"gana"
    }, 
    "papel":{
        "papel": "empate",
        "piedra":"gana",
        "tijera":"pierde"
    }, 
    "tijera": {
       "tijera":"empate",
       "papel": "pierde",
       "piedra":"gana" 
    }
}

def preguntaJugador ():
    print ("Elige\"piedra\",\"papel\" o \"tijera\"")
    eleccion=input()

    return eleccion

def preguntaMaquina ():
    eleccionMaquina= random.choice(["piedra", "papel","tijera"])
    return eleccionMaquina



eleccionJugador=preguntaJugador()
eleccionMaquina= preguntaMaquina ()
resultado=PiedraPapelTijera(eleccionJugador,eleccionMaquina)

salida=Template("el jugador ha elegido: $jugador, la maquina ha elegido: $maquina.\n el resultado ha sido: $resultado ")


print(
    salida.substitute(
        jugador= eleccionJugador,
        maquina= eleccionMaquina,
        resultado= resultado
    )
)

