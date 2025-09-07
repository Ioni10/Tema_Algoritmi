#Cautare liniara: intr-o lista de stringuri
def cautare_liniara(arr, target):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

lista_string = ["ana", "ion" , "paul"]
print(cautare_liniara(lista_string, "ion"))

