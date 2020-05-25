# persona

import random
from string import Template

class Persona:
    def __init__ (self, nombre, idioma = "es-es"):
        self.nombre = nombre

        if (idioma == "es-es"):

            self. presentacion=Template("Holi me llamo $nombre y tengo calcetines $color ")

        elif (idioma == "de"): 

            self.presentacion = Template("Hallo, ich bin $nombre und ich hasse $color Socken")

        else :

            self.presentacion = Template("😥")
                   

        self.calcetines = random.choice(["blancos", "magenta", "furcia"])

    def presentate (self):
               
        print (
            self.presentacion.substitute(
                nombre= self.nombre,
                color= self.calcetines 
            )

        )

