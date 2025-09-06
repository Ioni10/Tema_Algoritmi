#Cautare in matrice: 'binary search'
def cautare_in_matrice_binary(matrice, target):
    if not matrice:
        return False
    rows, cols = len(matrice), len(matrice[0])
    row, col = 0, cols -1
    while row < rows and col >=0:
        if matrice[row][col] == target:
            return "Gasit:", matrice[row][col]
        elif matrice[row][col] < target:
            row +=1
        else:
            col -=1
    return False

matrice = [
    [1,4,7],
    [2,5,9],
    [3,6,10]
]
print(cautare_in_matrice_binary(matrice, 5))