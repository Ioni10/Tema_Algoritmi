#Scriem algoritmul Knapsack 0/1:
def Knapsack(W, greutati, valori, n):
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif greutati[i-1] <= w:
                dp[i][w] = max(valori[i-1] + dp[i-1][w- greutati[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

greutatile = [2,3,4]
valori = [4,5,6]
capacitate = 5
n = len(greutatile)

print(Knapsack(capacitate, greutatile, valori, n))
"""
Explicatie: Knapsack algoritm pentru calcularea valori cea mai mare incadrata in capacitatea greutati
Sa ne gandim ca avem un ghiozdan cu o capacitate de 5 kg si avem n obiecte in cazul nostru 3
dp = [[0 for x in range(W+1)]for x in range(n+1)] - ne creazaa o matrice de 3 +1 randuri si 5 +1 coloane
am initia i si w ca indexi principali pentru matricea noastra 
dupa am pune conditiile ca daca indexul lui n si al lui W sunt 0 atunci si dp[i][w] = 0
Altfel dp[i][w] = formula adica maxim din valori -1 (excludem randurile cu 0 pentru ca in python listele incep cu indexare 0(adica ex range(5) = [0,1,2,3,4])
+ indexarile [i-1][W- greutati[i-1], dp[i-1][w]
Daca nu returnam valoare anterioara dp[i][w] = dp[i-1][w]
la final returnam dp[numar obiect][si greutatea lui]-> rezultatul fiind numarul maxim de valori acceptate de capacitate     
Ex stil tabel:

Obiecte | greutati | valori     |
  1     | 2kg      | 4lei       |
  2     | 3kg      | 5lei       | 
  3     | 4kg      | 6lei       |
 
 daca sa zicem ca luam al 3 lea obiect 5kg -4kg = 1kg deci nu am mai avea loc de nimic
 si am putea sa luam doar un obiect de 6 lei
 dar daca am lua 1obiect + al2obiect am aveam 2+3 = 5 care este 5 ==5(capacitate) adica la fix
 si am avea valori 4lei + 5lei = 9 lei !!!VARIANTA CORECTA!!!
     
 """