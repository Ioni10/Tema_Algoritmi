import heapq

def prim(graf, start):
    mst = []
    vizitat = set([start])
    heap = [(cost, start, vecin) for vecin , cost in graf[start]]
    heapq.heapify(heap)
    while heap:
        cost, frm, to = heapq.heappop(heap)
        if to not in vizitat:
            vizitat.add(to)
            mst.append((frm, to , cost))
            for vecin, c in graf[to]:
                if vecin not in vizitat:
                    heapq.heappush(heap, (c, to, vecin))
    return mst


def kruskal(noduri, muchii):
    parinte = {nod: nod for nod in noduri}

    def gaseste(x):
        while parinte[x] != x:
            x = parinte[x]
        return x

    def uneste(x,y):
        parinte[gaseste(x)] = gaseste(y)

    mst1 = []
    muchii.sort(key=lambda x: x[2])
    for u, v, cost in muchii:
        if gaseste(u) != gaseste(v):
            uneste(u, v)
            mst1.append((u,v, cost))
    return mst1

graf = {
    1: [(2, 1), (4, 4)],
    2: [(1, 1), (3, 2)],
    3: [(2, 2), (4, 3)],
    4: [(3, 3), (1, 4)]
}

print(prim(graf, 1))
rezultat_prim = prim(graf, 1)
print(kruskal(rezultat_prim))