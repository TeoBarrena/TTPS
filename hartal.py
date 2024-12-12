"""
2 -> indica cantidad casos de prueba
------------------------------------
14 -> indica cantidad de dias para el primer caso de prueba
3 -> indica cant. partidos politicos
3 -> indica patron de paros del 1er. part. politico
4 -> indica patron de paros del 2do. part. politico
8 -> indica patron de paros del 3er. part. politico
------------------------------------
100 -> indica cantidad de dias para el segundo caso de prueba
4 -> indica cant. partidos politicos
12 -> indica patron de paros del 1er. part. politico
15 -> indica patron de paros del 2do. part. politico
25 -> indica patron de paros del 3er. part. politico
40 -> indica patron de paros del 4to. part. politico
"""

def contar_dias_perdidos(T, casos):
    resultados = []
    
    for caso in casos:
        N = caso['N']
        patrones = caso['patrones']
        
        # Crear un arreglo para marcar días perdidos
        dias_perdidos = [False] * (N + 1)  # Usamos 1-indexing
        for h in patrones:
            # Marcar días de hartal
            for dia in range(h, N + 1, h):
                if dia % 7 != 6 and dia % 7 != 0:  # Ignorar viernes (6) y sábado (0)
                    dias_perdidos[dia] = True
        
        # Contar días perdidos
        dias_trabajo_perdidos = sum(dias_perdidos) #los valores True estan en 1, los False en 0, por eso se hace sum
        resultados.append(dias_trabajo_perdidos)
    
    return resultados

T = int(input()) #cantidad casos de prueba
casos = []

for _ in range(T):
    N = int(input()) #cantidad de dias
    P = int(input()) #cant partidos politicos
    patrones = [int(input()) for _ in range(P)] #ingresa cada partido politico su patron de huelga
    casos.append({'N':N, 'patrones':patrones})

resultados = contar_dias_perdidos(T,casos)
for resultado in resultados:
    print(resultado)