import random
import time
#Implementam algoritmul Heap Sort
def heapify(arr, n ,i):
    largest = i
    l = i*2 +1
    r = i*2 +2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i] , arr[0] = arr[0] , arr[i]
        heapify(arr, i, 0)
    return arr

x = [random.randint(0, 100000) for _ in range(100000)]

start = time.time()
rez= heap_sort(x)
end = time.time()
print("Timpul de executie la Heap Sort:", end - start,"secunde") #0.6019549369812012 secunde
print(rez)

y = [9,8,7,6,5,4,3,2,1]
start1 = time.time()
rez2= heap_sort(y)
end1 = time.time()
print("Timpul de executie la Heap Sort:", end1 - start1,"secunde")
print(rez2)
#Concluzie E cu mult mai lent cu 100000 de elemente random decat cu 9 elemente diferenta de 0.6019549369812012 secunde
# y se executa instant in 0,0 secunde