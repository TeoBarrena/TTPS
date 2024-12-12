

"""
------------INPUT------------
Hay n(<=10) figuras, una por cada linea
El primer caracter de una linea indica si la figura sera un rectangulo o un circulo (r o c)
Seguido de este caracter van los valores que describen esa figura
Rectangulo -> hay 4 valores reales designando las coordenadas x-y de los vertices de arriba a la izquierda y abajo a la derecha 
Circulo -> hay 3 valores reales designando las coordenadas x-y del centro y el radio
El final de la lista esta señalizado por una linea que contiene un solo "*"
El resto de las lineas contienen las coordenadas x-y, una por linea, de los puntos a testear.
El final de la lista esta indicado por un punto con las coordenadas 9999.9 9999.9, estos valores no deben ser incluidos en el output.

------------NOTAS------------
Los puntos que coincidan con el borde de una figura no son considerados dentro de la figura
Para el output -> los puntos y figuras deben aparecer en el orden en el que fueron ingresados en el input

------------OUTPUT------------
Para cada punto a testear escribir un mensaje de la forma:
Point i is contained in figure j para cada figura que contiene ese punto.
Si el punto no esta contenido en ninguna figura, se escribe un mensaje de la forma:
Point i is not contained in any figure
"""

class Rectangle():

    def __init__(self,x1,y1,x2,y2,idx):
        self.idx = idx
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def contains(self,x,y):
        return x > self.x1 and x < self.x2 and y < self.y1 and y > self.y2
    
    
class Circle():

    def __init__(self,x,y,r, idx):
        self.idx = idx
        self.x = x
        self.y = y
        self.r = r
        
    def contains(self,x,y):
        return (x-self.x)**2 + (y-self.y)**2 < self.r**2 #calcula si la distancia de x,y al centro es menor que la distancia de un punto del borde al centro (radio)
    
    

from sys import stdin, stdout

def main():
    figuras = []
    idx = 1
    while True:
        line = stdin.readline().split()
        if line[0] == "*":
            break

        type_figure = line[0] #r o c
        
        if type_figure == "r":
            figuras.append(Rectangle(float(line[1]),float(line[2]),float(line[3]),float(line[4]), idx)) #agarra x1,y1,x2,y2
        else:
            figuras.append(Circle(float(line[1]),float(line[2]),float(line[3]),idx)) #x, y, r
        idx += 1 #este para manejar el tema de figura x

    #aca se corto con el *
    
    puntos = []
    while True:
        line = stdin.readline().strip()
        if line == "9999.9 9999.9":
            break
        x,y = map(float, line.split())
        puntos.append((x,y))

    for i in range(len(puntos)):
        x,y = puntos[i]
        contained = False
        for figura in figuras:
            if figura.contains(x,y):
                stdout.write(f"Point {i+1} is contained in figure {figura.idx}\n")
                contained = True
        if not contained:
            stdout.write(f"Point {i+1} is not contained in any figure\n")

if __name__ == "__main__":
    main()


