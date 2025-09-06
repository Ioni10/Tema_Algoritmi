#Cautare binara: Intr-o lista de string.uri
def cautare_binara(arr, target):
    stanga = 0
    dreapta = len(arr) -1

    while stanga <= dreapta:
        mid = (stanga + dreapta)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            stanga = mid+1
        else:
            dreapta = mid-1

lista_string = ["ana", "ion" , "paul", "mihai", "george"]
lista_string.sort() #Cautarea binara functioneaza doar daca lista este sortata
#Daca nu am da .sort() , Output ar fi: None
print(cautare_binara(lista_string, "mihai"))