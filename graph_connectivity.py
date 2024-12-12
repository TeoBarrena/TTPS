"""Consider a graph G formed from a large number of nodes connected by edges.
G is said to be connected if a path can be found in 0 or more steps between any
pair of nodes in G. For example, the graph below is not connected because
there is no path from A to C.
This graph contains, however, a number of subgraphs that are connected,
one for each of the following sets of nodes: {A}, {B}, {C}, {D}, {E}, {A,B},
{B,D}, {C,E}, {A,B,D}
A connected subgraph is maximal if there are no nodes and edges in the
original graph that could be added to the subgraph and still leave it connected.
There are two maximal connected subgraphs above, one associated with the
nodes {A, B, D} and the other with the nodes {C, E}.
Write a program to determine the number of maximal connected subgraphs of a given graph.
Input
The input begins with a single positive integer on a line by itself indicating the number of the cases
following, each of them as described below. This line is followed by a blank line, and there is also a
blank line between two consecutive inputs.
The first line of each input set contains a single uppercase alphabetic character. This character
represents the largest node name in the graph. Each successive line contains a pair of uppercase
alphabetic characters denoting an edge in the graph.
The sample input section contains a possible input set for the graph pictured above.
Input is terminated by a blank line.
Output
For each test case, write in the output the number of maximal connected subgraphs. The outputs of
two consecutive cases will be separated by a blank line.
Sample Input
1
E
AB
CE
DB
EC
Sample Output
2"""

from sys import stdin, stdout
from collections import defaultdict

def dfs(graph, node, visited):
    visited.add(node)  #marco el nodo como visitado, primer caso marcaria A, dps en la recursion los otros nodos adyacentes a A
    for adyacente in graph[node]:  #se fija en los adyacentes de A, en este caso B y C, y mira si estan visitados, en caso de que no, hace la recursion
        if adyacente not in visited:
            dfs(graph, adyacente, visited)

def contar_nodos_conectados(graph, max_node):
    visited = set()  # Conjunto de nodos visitados
    conected = 0

    # Considerar todos los nodos desde A hasta max_node
    for node in range(ord('A'), ord(max_node) + 1): #lo pasa a ascii y va recorriendo desde A hasta el nodo más grnade
        node_char = chr(node)
        if node_char in graph and node_char not in visited: #por eso aca comprueba q este en graph 
            conected += 1
            dfs(graph, node_char, visited) #manda a hacer el dfs a partir de ese nodo q esta en graph y no esta visitado
        elif node_char not in graph and node_char not in visited:
            # si el nodo no está en el grafo, pero es parte del rango, contarlo como componente desconectado, ej: 1-E-AB-EC -> D no esta en el grafo pero es parte del rango, esta desconectado y lo cuenta y lo marca como visitado
            conected += 1
            visited.add(node_char)  
    return conected

#en el caso del input del ejemplo, A visita B, cuando el dfs ejecuta el nodo B visita al nodo D (DB) y no encuentra ninguno mas para visitar,
#a esa altura conected = 1, dps se fija en visited y ve que A, B y D estan visitados, agarra C que no esta visitado, incrementa conected y visita E, marcandolo como visitado
#no hay mas para buscar entonces termina la recursion y estan todos visitados, y termina devolviendo conected = 2

cases = int(stdin.readline().strip())  #número de casos
results = []
stdin.readline() #este por la primera linea en blanco
for _ in range(cases):
    
    max_node = stdin.readline().strip()  #agarra el nodo más grand
    
    graph = defaultdict(list)

    while True:
        line = stdin.readline().strip()
        if line == "":
            break
        if len(line) == 2:  
            u, v = line[0], line[1]
            if u != v:
                if v not in graph[u]:  # manejo de aristas para q no se agreguen repetidas en caso de ser x ej: CE y EC asi no se agregan dos veces a cada uno
                    graph[u].append(v)
                if u not in graph[v]:  # idem arriba
                    graph[v].append(u)
    result = contar_nodos_conectados(graph, max_node)
    results.append(result)

stdout.write("\n\n".join(map(str, results)) + "\n")
