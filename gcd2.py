
from sys import stdin, stdout

def gcd(a, b):
    while b != 0:
        a, b = b, a % b #gcd (a,b) = gcd(b, a mod b)
    return a

def mod_large_number(b, a):
    remainder = 0
    for digit in b:
        remainder = (remainder * 10 + int(digit)) % a  #multiplica por 10 para mover el dígito a la izquierda y calcula el mod con a, arma el num 
    return remainder

def main():
    try:
        t = int(stdin.readline())  
        for _ in range(t):
            a, b = stdin.readline().split()  #manejo entrada como string xq el numero b puede ser demasiado grande para los tipos de datos de python
            a = int(a)  

            if a == 0:
                stdout.write(b + "\n")  
            else:
                b_mod_a = mod_large_number(b, a)
                stdout.write(str(gcd(a, b_mod_a)) + "\n")
    except EOFError:
        pass

if __name__ == '__main__':
    main()
