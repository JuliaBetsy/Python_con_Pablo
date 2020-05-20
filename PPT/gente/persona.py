# persona

import random
from string import Template

class Persona:
    def __init__ (self, nombre):
        self.nombre = nombre
        self. presentacion=Template("Holi me llamo $nombre y tengo calcetines $color ")
        self.calcetines = random.choice(["blancos", "magenta", "furcia"])

    def presentate (self):
               
        print (
            self.presentacion.substitute(
                nombre= self.nombre,
                color= self.calcetines 
            )

        )

