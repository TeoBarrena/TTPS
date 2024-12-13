class Box:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_intersection(self, xs, ys, xr, yr):
        #dirección del viaje que realiza el rayo
        dx = xr - xs
        dy = yr - ys
        intersections = []

        #si dx = 0 se trata de una linea vertical
        #si dy = 0 se trata de una linea horizontal

        #t indica el porcentaje de la distancia recorrida desde el punto de origen del rayo hasta el punto de intersección en relación a la dirección del rayo, porcentaje basado en relación al rayo, no a la caja
        #t < 0 -> indica que la intersección ocurre DETRÁS del origen del rayo, por ende no se considera 
        #0 < t < 1 -> indica que la intersección ocurre ENTRE el origen del rayo y el punto final del rayo
        #t = 1 -> indica que la intersección ocurre EXACTAMENTE en el punto final del rayo
        #t > 1 -> indica que la intersección ocurre DESPUÉS del punto final del rayo

        #left
        if dx != 0:
            t = (self.x1 - xs) / dx 
            y_intersect = ys + t * dy
            if t >= 0 and self.y1 <= y_intersect <= self.y2:
                intersections.append((t, self.x1, y_intersect, "left"))

        #right
        if dx != 0:
            t = (self.x2 - xs) / dx
            y_intersect = ys + t * dy
            if t >= 0 and self.y1 <= y_intersect <= self.y2: #si se da que t >= 0, por ende el rayo esta en la direccion correcta, y el punto de interseccion esta dentro del rango del eje y de la caja
                intersections.append((t, self.x2, y_intersect, "right")) 

        #bottom
        if dy != 0:
            t = (self.y1 - ys) / dy
            x_intersect = xs + t * dx
            
            if t >= 0 and self.x1 <= x_intersect <= self.x2:
                intersections.append((t, x_intersect, self.y1, "bottom"))

        #top
        if dy != 0:
            t = (self.y2 - ys) / dy
            x_intersect = xs + t * dx #2
            if t >= 0 and self.x1 <= x_intersect <= self.x2:
                intersections.append((t, x_intersect, self.y2, "top"))

        intersections.sort() #ordenas por el que tiene menor t -> el que esta mas cerca
        
        t, x, y, side = intersections[0]
        

        #analiza casos esquinas
        if x == self.x1 and y == self.y1:
            return "bottom-left"
        if x == self.x1 and y == self.y2:
            return "top-left"
        if x == self.x2 and y == self.y1:
            return "bottom-right"
        if x == self.x2 and y == self.y2:
            return "top-right"

        return side

from sys import stdin,stdout
def main():

    x1, x2, y1, y2 = map(int, stdin.readline().split())
    box = Box(x1, x2, y1, y2)
    xs, ys, xr, yr = map(int, stdin.readline().split())

    result = box.get_intersection(xs, ys, xr, yr)
    stdout.write(result)

if __name__ == "__main__":
    main()
