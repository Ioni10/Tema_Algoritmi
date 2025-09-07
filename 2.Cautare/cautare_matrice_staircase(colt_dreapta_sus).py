#Cautare intr-o matrice sortata, din coltul dreapta sus
def cautare_matrice_staircase(matrice, target):
    if not matrice or not matrice[0]:
        return False
    randuri = len(matrice)
    coloane = len(matrice[0])
    i,j = 0, coloane -1
    while i < randuri and j >= 0:
        if matrice[i][j] == target:
            return "Gasit",matrice[i][j]
        elif matrice[i][j] > target:
            j -=1
        else:
            i +=1
    return False

matrice = [[1,4,7],
           [2,5,9],
           [3,6,10]
           ]

print(cautare_matrice_staircase(matrice, 5))