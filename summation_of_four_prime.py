

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1) #para inicializar la criba 
    is_prime[0], is_prime[1] = False, False #0 y 1 no son primos
    for num in range(2, limit): #itera hasta raiz cuadrada de n
        if is_prime[num]: #se fija si el num sigue marcado como primo
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False #marca sus multiplos en False
    primes = [num for num, prime in enumerate(is_prime) if prime]   #agarra los q qdaron en True, osea son
    return primes

def is_prime(n, small_primes):
    if n < 2:
        return False
    for prime in small_primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True
        
def find_four_primes(n, primes):

    if n % 2 == 0:
        for p1 in primes:
            p2 = n - 4 - p1 #aca hace el uso de conjetura de Goldbach
            if is_prime(p2, primes): #se fija si el resultado es un primo, xq se puede dar q de un numero no primo entonces no se deberiaa retornar
                return [2, 2, p1, p2]
    
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                p4 = n - (p1 + p2 + p3)
                if p4 > 1 and is_prime(p4, primes):
                    return [p1, p2, p3, p4]

import math

def main():

    while True:
        try:
            n = int(input().strip())
            if n < 8:
                print("Impossible.") #cualq num < 8 no puede ser suma de 4 nums primos
            else:
                limit = int(math.sqrt(n)) + 1 #aca hace uso de la crib  a de Erostotenes v2, que utiliza los primos hasta la raiz cuadrada de n, xq el n puede ser hasta 10000000
                primes = sieve_of_eratosthenes(limit)
                result = find_four_primes(n, primes)
                if result:
                    print(" ".join(map(str, result)))
                else:
                    print("Impossible.")
        except EOFError:
            break

if __name__ == '__main__':
    main()