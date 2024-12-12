from sys import stdin, stdout

#para inicializar una unica vez la matriz para cad caso de prueba
def init_dist(c, calles):
    INF = float('inf')
    dist = [[INF for _ in range(c)] for _ in range(c)]  

    for i in range(c):
        dist[i][i] = 0  # inicializar la diagonal en 0 porque la dist de un nodo a sí mismo es 0

    # para cargar los valores que se obtuvieron en lista calles
    for c1, c2, d in calles:
        dist[c1 - 1][c2 - 1] = min(dist[c1 - 1][c2 - 1], d)  # mantener el menor db
        dist[c2 - 1][c1 - 1] = min(dist[c2 - 1][c1 - 1], d)  # xq es grafo no dirigido

    #print("Despues de cargar las calles")
    #for d in dist:
    #    print(d)

    #hasta aca esta bien
    return dist

def floyd_warshall(c, dist):
    for k in range(c):  # k -> nodo intermedio
        for i in range(c):  # i -> nodo origen
            for j in range(c):  # j -> nodo destino
                dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j])) 
    return dist

case_number = 1
output = []

while True:
    line = stdin.readline().strip()
    if line == "0 0 0":
        break

    c, s, q = map(int, line.split())
    
    calles = []
    consultas = []
    
    # obtiene los inputs de las calles 
    for _ in range(s):
        c1, c2, d = map(int, stdin.readline().strip().split())
        calles.append((c1, c2, d))

    # obtinee inputs de las consultas
    for _ in range(q):
        c1, c2 = map(int, stdin.readline().strip().split())
        consultas.append((c1, c2))
    
    output.append(f"Case #{case_number}")
    case_number += 1

    dist = init_dist(c, calles)  # inicializar una vez sola la matriz
    dist = floyd_warshall(c, dist)  # cargarla una sola vez, para un  mismo caso de prueba

    for c1, c2 in consultas:
        resultado = dist[c1 - 1][c2 - 1] # se fija directamente el valor cargado en esa pos
        if resultado != float('inf'): 
            output.append(str(resultado))
        else:
            output.append("no path")

    output.append("")  # Línea en blanco entre casos

stdout.write("\n".join(output).strip() + "\n")