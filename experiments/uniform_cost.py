import heapq
import time

def uniform_cost(graph, start, goal):
    t0 = time.time()
    pq = [(0, start)]
    visited = 0
    dist = {start: 0}
    prev = {}

    while pq:
        cost, node = heapq.heappop(pq)
        visited += 1

        if node == goal:
            break

        for neigh, w in graph.neighbors(node):
            new_cost = cost + w
            if new_cost < dist.get(neigh, float("inf")):
                dist[neigh] = new_cost
                prev[neigh] = node
                heapq.heappush(pq, (new_cost, neigh))

    t1 = time.time()

    return {
        "cost": dist.get(goal, float("inf")),
        "visited": visited,
        "time": t1 - t0
    }
