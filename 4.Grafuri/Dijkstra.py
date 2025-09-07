import heapq


def Dijkstra(graf, start):
    dist = {nod: float('inf') for nod in graf}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        curent_dist , nod = heapq.heappop(heap)
        for vecin , cost in graf[nod]:
            if dist[nod] + cost < dist[vecin]:
                dist[vecin] = dist[nod] + cost
                heapq.heappush(heap, (dist[vecin], vecin))
    return dist

graf = {'A': [('B',1), ('C',2), ('D', 3)],
        'B': [('B',4), ('C',5), ('D', 6)],
        'C': [('A',7), ('B',8), ('D', 9),('F',10)],
        'D': [('A',11), ('B',12),('D',13),('E',14)],
        'E': [('A',15),('B',16) ,('C',17), ('D',18)],
        'F': [('B',19),('C',20),('D',21),('E',22)]}

dist = Dijkstra(graf, 'A')
print("Dijkstra:", dist)