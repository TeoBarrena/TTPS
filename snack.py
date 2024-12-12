tabla = [{"1":4.00},{"2":4.50}, {"3":5.00},{"4":2.00},{"5":1.50}]
try:
    x,y = map(int, input().split())
    total = ((tabla[x-1][str(x)])*y)
    print(f"Total: R$ {total:.2f}")
except ValueError:
    print("Caracter no valido")
except IndexError:
    print("Codigo no cargado en el sistema")