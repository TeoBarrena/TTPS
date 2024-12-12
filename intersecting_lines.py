

"""
-------INPUT-------
La primera linea contiene un entero N (1 <= N <= 10) describiendo el numero de lineas que son representadas
Las siguientes N lineas tienen 8 enteros. Estos enteros representan las coordenadas de los cuatro puntos en el plano, en el orden x1,y1, x2, y2, x3,y3 x4,y4.
Estos puntos representan dos lineas en el plano. 
Una linea -> x1,y1, x2,y2
La otra linea -> x3,y3, x4,y4
El punto x1,y1 es diferente de x2,y2. Lo mismo con x3,y3 y x4,y4

------------OUTPUT------------
Hay N+2 lineas de output
La primer linea es "INTERSECTING LINES OUTPUT"
Las siguientes N lineas son de la forma:
    none, line, or point
Si la interseccion es un punto -> "POINT x y"
Si la interseccion es una linea -> "LINE"
Si no hay interseccion -> "NONE"
La ultima linea es "END OF OUTPUT"0 
"""

class Line():

    def __init__(self, x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_intersection_point(self,l2):    

        m1 = self.get_pendiente()
        m2 = l2.get_pendiente()

        if m1 is None: #este caso seria que la linea 1 sea vertical, tmb se evita el caso donde el divisor sea 0
            x = self.x1 
            y = m2 * (x - l2.x1) + l2.y1
        elif m2 == 0: #caso donde linea 2 es vertical
            x = l2.x1
            y = m1 * (x - self.x1) + self.y1
        else: #ninguna de las dos son verticales
            b1 = self.y1 - m1 * self.x1
            b2 = l2.y1 - m2 * l2.x1

            x = (b2-b1) / (m1-m2) #interseccion en x
            y = m1 * x + b1 #interseccion en y

        return x,y
        

    def get_pendiente(self):
        if self.x2 == self.x1:
            return None
        return (self.y2-self.y1) / (self.x2-self.x1)

    def equal_lines(self,l2):
        return (self.y1 - l2.y1) * (self.x2 - self.x1) == (self.x1 - l2.x1) * (self.y2 - self.y1) #

    def intersect(self,l2):

        if self.get_pendiente() == l2.get_pendiente(): #en caso de tener = pendientes, o se trata d euna paralela o de una misma linea
            if self.equal_lines(l2): #se fija si l1.x1 = l2.x1 y l1.y1 = l2.y1, basicmanente si tienen el mismo inicio
                print("LINE")
            else:
                print("NONE") #sino, se trata de lineas paralelas
        else: # en caso de no tener la misma pendiente , en algun momento se chocan, se calcula ese punto de choque
            x,y = self.get_intersection_point(l2)
            print(f"POINT {x:.2f} {y:.2f}")
        
from sys import stdin, stdout

def main():
    lines = []
    n = int(stdin.readline()) # numero de lineas q ingresaran

    for _ in range(n):
        x1,y1,x2,y2,x3,y3,x4,y4 = map(int, stdin.readline().split())
        lines.append((Line(x1,y1,x2,y2), Line(x3,y3,x4,y4))) #list ade tuplas
    
    print("INTERSECTING LINES OUTPUT")
    for l1,l2 in lines: #agarra de a dos lineas y solamente se fija en l1
        l1.intersect(l2)
    print("END OF OUTPUT")

if __name__ == "__main__":
    main()