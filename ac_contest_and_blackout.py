

"""
------------------INPUT-----------------
La entrada comienza con el número de casos de prueba, T (1 < T < 15) en una línea.
Luego siguen T casos de prueba
La primer linea de cada caso de prueba contiene dos números separados por un espacio:
N (3<N<100), numero de escuelas en la ciudad, y M numero de posibles conexiones entre ellas.
A continuacion hay M lineas que contienen tres numeros A,B,C donde C -> es el costo de la conexión (1<C<300) entre las escuelas A y B. 
Las escuelas estan numeradas en el rango 1 a N

------------------OUTPUT-----------------
Para cada caso de prueba imprime una linea de salida.
Contiene dos números separados por un espacio: el costo de los dos planes de conexión más baratos.
"""




from sys import stdin, stdout

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, u):
        if self.parent[u] != u: 
            self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u]

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        if x != y: #se fija si los representantes de x e y estan en conjuntos separados, si es asi los une
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
            elif self.rank[x] < self.rank[y]:
                self.parent[x] = y
            else:
                self.parent[y] = x
                self.rank[x] += 1

def kruskal_mst(n, conexiones):
    conexiones.sort(key=lambda x: x[2])  # modifica el alg de ksurkal ordenando por peso de la arista
    uf = UnionFind(n)
    mst_cost = 0
    mst_conexiones = []
    
    for u, v, cost in conexiones:
        if uf.find(u) != uf.find(v):  # comprueba q no se forme un ciclo
            uf.union(u, v)
            mst_cost += cost
            mst_conexiones.append((u, v, cost))
        if len(mst_conexiones) == n - 1:  # para verificar q se cumple el criterio de conectividad se necesitan V-1 aristas (en este caso V -> n)
            break

    if len(mst_conexiones) != n - 1:
        return float('inf'), []  # por eso aca devuelve infinito si da <> n-1

    return mst_cost, mst_conexiones

def second_mst(n, conexiones, mst_conexiones): #mst_conexiones tiene las resultantes del 1ro, entonces en el for va a ir sacando 1 x 1 y probando con otros caminos para obtener el2do más barato
    mst_cost_2 = float('inf')

    for conexion in mst_conexiones: 
        uf = UnionFind(n)
        cost = 0
        cant = 0

        for u, v, c in conexiones:
            if (u, v, c) == conexion:  
                continue
            if uf.find(u) != uf.find(v): # para que no se generen ciclos
                uf.union(u, v)
                cost += c
                cant += 1

        if cant == n - 1:
            mst_cost_2 = min(mst_cost_2, cost)

    return mst_cost_2

result = ""
try:
    while True:
        line = stdin.readline().strip()
        if line == "":
            break
        
        T = int(line)  # num casos pruebas
        for _ in range(T):
            n, m = map(int, stdin.readline().strip().split())  # n -> escuelas, m -> conexiones
            conexiones = []
            
            for _ in range(m):
                a, b, c = map(int, stdin.readline().strip().split())                    
                conexiones.append((a, b, c))

            mst_cost, mst_conexiones = kruskal_mst(n, conexiones)
            
            mst_cost_2 = second_mst(n, conexiones, mst_conexiones)

            result += f"{mst_cost} {mst_cost_2}\n"

    stdout.write(result)

except Exception as e:
    print(str(e))









