import math 

print("Holi Mundo")
def my_function(nombre, años):
    print("Holi " + nombre + ", tienes ")
    print ( años)
    if (años > 1): #then
        print ("años")
    else: 
        print ("año")
#final de my_function 
# El cuadrado de una hipotenusa de un triangulo rectangulo es igual a la suma de los dos catetos al cuadrado
# h=sqrt(c^2+c^2  )

def pitagoras (cateto1, cateto2):
    return math.sqrt(cateto1**2+cateto2**2)


my_function ("Quevedo", 1) 



