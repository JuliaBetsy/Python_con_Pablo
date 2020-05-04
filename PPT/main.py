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

    jugadas[eleccion] += 1

    return eleccion

def preguntaMaquina ():

    if jugadas ["tijera"] >= jugadas ["papel"]:
        # elegir entre papel o piedra
        if jugadas ["papel"]> jugadas ["piedra"]:
            return "piedra"
        else : 
            return "papel"

    else : 
        if jugadas ["tijera"]>= jugadas["piedra"]:
            return "piedra"
        else: 
            return "tijera"    


def preguntaMaquinaRandom ():
    eleccionMaquina= random.choice(["piedra", "papel","tijera"])
    return eleccionMaquina

def jugar():
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
    # if resultado == "gana":
    #     partidas ["gana"]+= 1
    # elif resultado == "empate":
    #     partidas ["empate"]+= 1
    # elif resultado == "pierde":
    #     partidas ["pierde"] += 1 

    partidas[resultado] += 1
    
partidas = {
    "gana": 0,
    "empate": 0,
    "pierde": 0
}

jugadas = {
    "piedra": 0,
    "papel": 0,
    "tijera": 0
}



contador =Template("G:$ganadas E:$empatadas P:$perdidas")

    

salida = False 
while not (salida):
    print(" puedes \"jugar\"o \"salir\" \n>", end=":D ")
    lectura = input( ) 
    if (lectura== "salir"):
        print("Adeus")
        salida = True 

    elif (lectura== "jugar"):
        jugar()
        print(
            contador.substitute(
                ganadas= partidas ["gana"],
                empatadas= partidas ["empate"],
                perdidas= partidas ["pierde"]
            )
        )

    else :
        print ("no entiendo")

