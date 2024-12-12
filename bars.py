"""
Input
The first line of the input contains an integer,t, 0 ≤ t ≤ 50, indicating the number of test cases. For
each test case, three lines appear, the first one contains a number n, 0 ≤ n ≤ 1000, representing the
length of the bar we want to obtain. The second line contains a number p, 1 ≤ p ≤ 20, representing the
number of bars we have. The third line of each test case contains p numbers, representing the length
of the p bars.

Output
For each test case the output should contain a single line, consists of the string ‘YES’ or the string ‘NO’,
depending on whether solution is possible or not.

-Primer linea tiene la cantidad de número de casos (entre 0 y 50).

-Para cado caso la primer linea representa el número de tamaño que se quiere obtener de la barra resultante (entre 0 y 1000).
-La segunda línea representa el número de barras que se tiene para cada caso (entre 1 y 20).
-La tercer linea contiene p números que representan el tamaño de las p barras.

Sample Input
4
25
4
10 12 5 7
925
10
45 15 120 500 235 58 6 12 175 70
120
5
25 25 25 25 25
0
2
13 567

Sample Output
NO
YES
NO
YES
"""

def can_get_size_expected(size_expected,bar_sizes):
    dp = [False] * (size_expected + 1) # se hace de tamaño size_expected para poder cubrir desde 0 hasta el size correspondiente
    dp[0] = True

    for bar in bar_sizes:
        for current_size in range(size_expected, bar - 1, -1):
            if dp[current_size - bar]:
                dp[current_size] = True

    return "YES" if dp[size_expected] else "NO"


t = int(input()) #t casos
results = []

for _ in range(t):

    size_expected = int(input()) #est va de 0-1000
    num_bars = int(input()) #de 1 a 20
    bar_sizes = list(map(int, input().split())) 

    result = can_get_size_expected(size_expected,bar_sizes)
    results.append(result)

for result in results:
    print(result)


