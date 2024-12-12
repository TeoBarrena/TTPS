"""Some people think that the bigger an elephant is, the smarter it is. To disprove this, you want to take
the data on a collection of elephants and put as large a subset of this data as possible into a sequence
so that the weights are increasing, but the IQ’s are decreasing.

Input
The input will consist of data for a bunch of elephants, one elephant per line, terminated by the endof-file. The data for a particular elephant will consist of a pair of integers: the first representing its size
in kilograms and the second representing its IQ in hundredths of IQ points. Both integers are between
1 and 10000. The data will contain information for at most 1000 elephants. Two elephants may have
the same weight, the same IQ, or even the same weight and IQ.

Output
Say that the numbers on the i-th data line are W[i] and S[i]. Your program should output a sequence
of lines of data; the first line should contain a number n; the remaining n lines should each contain
a single positive integer (each one representing an elephant). If these n integers are a[1], a[2],..., a[n]
then it must be the case that
W[a[1]] < W[a[2]] < ... < W[a[n]]
and
S[a[1]] > S[a[2]] > ... > S[a[n]]
In order for the answer to be correct, n should be as large as possible. All inequalities are strict:
weights must be strictly increasing, and IQs must be strictly decreasing.
There may be many correct outputs for a given input, your program only needs to find one.

Sample Input
6008 1300
6000 2100
500 2000
1000 4000
1100 3000
6000 2000
8000 1400
6000 1200
2000 1900

Sample Output
4
4
5
9
7"""
#stdout.write
from sys import stdin, stdout 

def get_lis(seq,maxN):
    dp = [] #almacena para cada indice la subsecuencia más larga posible
    prev = [] #este vaa a guardar los indices de los predecesores, init en -1
    ans = 0

    for i in range(maxN):
        dp.append(1) #inicializo a todas las posiciones en 1
        prev.append(-1) #inicializo en -1 indicando q nadie lo predecede
    
         #este indice sirve para recorrer cada posicon de la seq
        for j in range(0,i):
            if (seq[j][0] < seq[i][0]) and (seq[j][1] > seq[i][1]) and (dp[i] < dp[j] + 1):#tambien [j][0] compara por peso y [j][1] compara por iq #dp[i]<dp[j]+1 -> se fija si agregando uno a la cantidad de numeros en la seq mas grande va a aumentar el tamaño, en caso de que si, me sirve xq indica que se encontro una subsecuencia mas larga que la actual  
                dp[i] = dp[j] + 1 #aumento el tamaño de la sub. más larga
                prev[i] = j #almaceno el indice, indicando el nuevo predecesor
        
        #aca tuve q poner <= para que me de el output igual al del pdf               esta parte es para comprar el id
        if (dp[ans] <= dp[i]) or (dp[i] == dp[ans] and seq[i][1] < seq[ans][1]) : # primer analisis = si la subs[ans] < subs[i] -> establece en ans el indice de la nueva subs más larga, ó si las subs son iguales, pero la que se esta comparando con el indice i, si tiene menos IQ que la de la subs con indice ans, se establece ans = i
            ans = i  # si encontré una subsecuencia más larga o un empate con menor IQ
    return ans, dp, prev #devuelvo indice para poder rearmarla, y el dp y prev


elephants = [] #este guarda la info de los elefantes, peso e iq


idx= 1

for line in stdin:
    weight, iq = map(int, line.strip().split())
    elephants.append((weight, iq, idx ))
    idx+=1

elephants.sort(key=lambda x: (x[0], -x[1])) #ordena a los elefantes por peso asc e iq desc

lis,dp,prev = get_lis(elephants,len(elephants)) #lis tiene el indice ans, dp y prev los arreglos

lis_seq = []
while lis != -1:
    lis_seq.append(elephants[lis])
    lis = prev[lis] #aca obtngo el predecesor correspondiente

lis_seq.reverse()

print(len(lis_seq))
for lis in lis_seq:
    print (lis[2])

#captura que muestre la barra del acepted y el codigo en un txt
#apellido y nombre de problema