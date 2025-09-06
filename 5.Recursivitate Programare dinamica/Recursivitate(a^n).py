#Functie recursiva calcul putere (A^n) :
def putere(A, n):
    if n == 0:
        return 1
    else:
        return A * putere(A, n- 1)

print(putere(2, 10))