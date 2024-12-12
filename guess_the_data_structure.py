import sys
import heapq
from collections import deque

# Leer todas las líneas de la entrada hasta el EOF
input_lines = sys.stdin.read().splitlines()

while input_lines:
    if len(input_lines) == 0:
        break  # Si no hay más líneas, salir del bucle

    # Intentar convertir la primera línea en un número
    try:
        n = int(input_lines.pop(0))  # Obtener el número de operaciones
    except ValueError:
        break  # Si no es un número válido, salir

    # Verificar si n es 0, ya que no hay operaciones que procesar
    if n == 0:
        print("impossible")
        break

    is_stack, is_queue, is_priority_queue = True, True, True
    stack, priority_queue = [], []
    queue = deque()

    for _ in range(n):
        if not (is_stack or is_queue or is_priority_queue):
            break  # No es necesario seguir procesando si todas son falsas
        operation, value = map(int, input_lines.pop(0).split())
        #print(F"OPERATION: {operation}, VALUE: {value}")
        if operation == 1:
            if is_stack:
                stack.append(value)
            if is_queue:
                queue.append(value)
            if is_priority_queue:
                heapq.heappush(priority_queue,-value) #insertar con valor negativo porque la heapq ordena como min-heap
            """print("OPERACION 1")
            print(f"Stack: {stack}")
            print(f"Queue: {queue}")
            print(f"Priority queue: {priority_queue}")"""
        elif operation == 2:

            if is_stack:
                if stack and stack.pop() != value:
                    is_stack = False
                elif not stack:
                    is_stack = False
            
            if is_queue:
                if queue and queue.popleft() != value:
                    is_queue = False
                elif not queue:
                    is_queue = False
            
            if is_priority_queue:
                if priority_queue and -heapq.heappop(priority_queue) != value:
                    is_priority_queue = False
                elif not priority_queue:
                    is_priority_queue = False
    """print(f"Stack: {stack}")
    print(f"Queue: {queue}")
    print(f"Priority queue: {priority_queue}")"""
    #para determinar que estructura es posible
    suma = sum([is_stack, is_queue, is_priority_queue])
    #print(f"Posibles: {posibles}")
    if suma > 1:
        print("not sure")
    elif suma == 0:
        print("impossible")
    elif is_stack:
        print("stack")
    elif is_queue:
        print("queue")
    elif is_priority_queue:
        print("priority queue")