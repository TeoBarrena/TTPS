
"""
-------INPUT-------
La primer linea de input -> numero de routers en la red (n).
Siguientes n lineas -> contiene descripcion de la red
Cada una de las n lineas siguientes -> id del router, seguido de un "-" y una lista de routers a los que está conectado, separados por una coma
La lista esta ordenada en orden ascendente
La siguiente linea contiene un numero de rutas (m) a determinar
Las m lineas consecutivas contiene el router de inicio y finalizacion separados por un espacio en blanco
Los datos del input pueden contener descripciones de muchas redes

-------OUTPUT-------
Para cada red, se imprime una linea con 5 "-"
Despues para cada ruta se imprime una lista de los routers por donde paso la info desde el principio al final
En caso de que pasar la info sea imposible (no connection exists) se imprime 'connection impossible'. 
En el caso de que haya muchas rutas con el mismo costo se imprime la que tiene la que tiene IDs más bajos

-------NOTAS-------
El numero de routers es menor o igual a 300, y hay al menos 2 routers en la red. Cada uno de los routers tiene una lista de no más de 50 routers que "ve".
"""

from sys import stdin, stdout
from collections import deque

def bfs(routers, ruta):
    #print(f"Ruta: {ruta}")
    distancias = [float("inf")] * (len(routers) + 1) 
    prev = [-1] * (len(routers) + 1)  # para poder armar el camino
    cola = deque()

    cola.append(ruta[0])
    distancias[ruta[0]] = 0

    while cola:
        t = cola.popleft()
        for w in routers[t]: #para cada w adyacente a t
            if distancias[w] == float("inf"): #esto indica q no se visito el nodo
                distancias[w] = distancias[t] + 1
                prev[w] = t  # para poder ir armando el camino
                cola.append(w)

    if distancias[ruta[1]] == float("inf"):
        return "connection impossible"
    
    camino = []
    actual = ruta[1] #aca agarra el nodo destino
    while actual != -1:
        camino.append(actual) 
        actual = prev[actual] 
    
    camino.reverse()  # para que quede en orden de inicio a fin
    return camino

result = ""

try:
    while True:
        line = stdin.readline().strip()
        if line == "":
            break
        
        n = int(line) #lee el numero de routers de una red
        if n <= 0:
            continue  # Salta si no hay routers
        routers = {} #diccionario para manejar, cada router tiene su lista de routers que ve

        for _ in range(n):
            line = stdin.readline().strip()
            id_router, routers_vistos = line.split("-")
            id_router = int(id_router)
            if routers_vistos.strip():  # por el caso 2- x ej.
                routers[id_router] = list(map(int, routers_vistos.split(","))) #cargar en routers el id, y su lista de routers
            else:
                routers[id_router] = []
        
        m = int(stdin.readline().strip()) #m casos a determinar
        if m <= 0:
            continue  # Salta si no hay casos
        rutas_a_determinar = []
        for _ in range(m):
            inicio, fin = map(int, stdin.readline().strip().split())
            rutas_a_determinar.append((inicio, fin))
        

        for router in routers:
            routers[router].sort()

        result += "-" * 5 + "\n"
        for ruta in rutas_a_determinar:
            #if ruta[0] not in routers or ruta[1] not in routers:
            #    result += "connection impossible\n"  
            #    continue
            camino = bfs(routers, ruta)
            if isinstance(camino, str):  
                result += camino + "\n"  
            else:
                result += " ".join(map(str, camino)) + "\n" 

except Exception as e:
    result += f"Error: {str(e)}\n"  # Captura el error y lo muestra

stdout.write(result)