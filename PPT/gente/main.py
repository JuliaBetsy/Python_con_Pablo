import persona
from string import Template
from discoteca import Discoteca 

lista=[]
nombres = ["Juan", "Pepe", "Dieter", "technoviking", "chayanne"] 
#hain es una discoteca muy perversa
hain = Discoteca (nombre = "Hain")

for nombre in nombres:
    print (nombre)

    aux = (persona.Persona (nombre))
    #lista.append (aux)
    hain.añadirColaEntrar (aux)

for tic in range (0, 18):
    print (tic)
    hain.intentarPasar ()


    