import random 

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
    "tijeras": {
       "tijera":"empate",
       "papel": "pierde",
       "piedra":"gana" 
    }
}

def preguntaJugador ():
    return "papel"

def preguntaMaquina ():
    eleccionMaquina= random.choice(["piedra", "papel","tijera"])
    return eleccionMaquina

print (
    PiedraPapelTijera(preguntaJugador(),preguntaMaquina())
)


