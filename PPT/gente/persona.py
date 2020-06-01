# persona

import random
from string import Template

MAX_HIGADO = 100


class Persona:
    def __init__ (self, nombre = "el señor tofu", idioma = "es-es"):
        self.nombre = nombre
        self.higado = 0
        self.dinero = 100
        
        if (idioma == "es-es"):

            self. presentacion=Template("Holi me llamo $nombre y tengo calcetines $color ")

        elif (idioma == "de"): 

            self.presentacion = Template("Hallo, ich bin $nombre und ich hasse $color Socken")

        else :

            self.presentacion = Template("😥")
                   

        self.calcetines = random.choice(["blancos", "magenta", "furcia"])



    def beber (self, bebida, coste):

        if (coste <= self.dinero):
            self.dinero = self.dinero - coste
            self.higado = self.higado + bebida  
            
        


    def presentate (self):
               
        print (
            self.presentacion.substitute(
                nombre= self.nombre,
                color= self.calcetines 
            )

        )

aux = Persona ()
aux.beber (10,0)
print ("fin de la prueba")
