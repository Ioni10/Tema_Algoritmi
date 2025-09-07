import time



#Implementam MergeSort
def merge_sort(arr):
    if len(arr)> 1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        merge_sort(l)
        merge_sort(r)
        i=j=k=0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
                k+=1
            else:
                arr[k] = r[j]
                j+=1
                k+=1
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1
    return arr

#Implementam QuickSort :

def quick_sort(arr):
    if len(arr) < 1:
        return arr
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x < pivot]
    great = [x for x in arr[1:] if x >= pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(great)

#Implementam HeapSort :

def heapify(arr, n ,i):
    radacina = i # Nu mai imi venea cum se scria :))
    l = i*2 +1
    r = i*2 +2
    if l < n and arr[l] > arr[radacina]:
        radacina = l
    if r < n and arr[r] > arr[radacina]:
        radacina = r
    if radacina != i:
        arr[i], arr[radacina] = arr[radacina] , arr[i]
        heapify(arr, n, radacina)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1, -1,-1):
        heapify(arr, n, i)
    for i in range(n-1, 0 ,-1):
        arr[i] , arr[0] = arr[0], arr[i]
        heapify(arr, i ,0)
    return arr


#Avem 3 vectori :
a = [1,2,3,4,5,6,7,8,9] # Vector crescator

b = [9,8,7,6,5,4,3,2,1] # Vector descrescator

c = [3,1,4,5,2,8,6,7,9] # Vector random

#Testam timpi de executie:
#MergeSort
start_merge = time.time()
merge_sort(a)
merge_sort(b)
merge_sort(c)
end_merge = time.time()

#QuickSort
startquick = time.time()
quick_sort(a)
quick_sort(b)
quick_sort(c)
endquick = time.time()

#HeapSort
start_heap = time.time()
heap_sort(a)
heap_sort(b)
heap_sort(c)
end_heap = time.time()

#Afisarile
print("Timpi de executie pentru Merge Sort", end_merge-start_merge, "secunde")
print("Timpi de executie pentru Quick Sort", endquick-start_merge, "secunde")
print("Timpi de executie pentru Heap Sort", end_heap-start_heap, "secunde")
print("Concluzie cei 3 algoritmi se executa instant")