import persona
from string import Template

lista=[]
nombres = ["Juan", "Pepe", "Dieter", "technoviking", "chayanne"] 
#hain es una discoteca muy perversa
hain=[]

def escupir (persona):
    print ("heute leider nicht " + persona.nombre)

for nombre in nombres:
    print (nombre)

    aux = (persona.Persona (nombre))

    lista.append (aux)

pass

for p in lista:
    p.presentate ()
    if (p.calcetines != "blancos"):
        hain.append (p)
    else :
        escupir (p) 

pass

    