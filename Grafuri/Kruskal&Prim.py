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

