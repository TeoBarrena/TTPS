
def is_jolly(lista):
    size = int(lista[0]) #especifica la cantidad de numeros que hay en la secuencia
    if size == 1:
        return True
    allValues = [False] * (size-1) #genero un arreglo con todos los valores en False
    numbers = lista[1:size+1] #obtiene los numeros de la secuencia
    numbers = [int(x) for x in numbers]
    for i in range(size-1):
        result = abs((numbers[i] - numbers[i+1])) - 1 #result indica la posicion a la que se va a guardar la diferencia
        try:
            if (result >= size) or (allValues[result] == True):
                return False
            allValues[result]=True
        except:
            return False 
    return True

try:
    entradas = []
    print("Introduce secuencias (una por línea, deja una línea vacía para terminar):")
    
    # Leer múltiples entradas hasta recibir una línea vacía
    while True:
        entrada = input()
        if entrada.strip() == "":  # Salir del loop si la entrada es una línea vacía
            break
        entradas.append(entrada.split())  # Dividir y guardar la entrada en la lista
    
    # Procesar cada secuencia
    for lista in entradas:
        if is_jolly(lista):
            print("Jolly")
        else:
            print("Not jolly")
except Exception as e:
    print(f"Error: {e}")
