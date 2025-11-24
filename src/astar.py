import heapq
import time

def astar(graph, start, goal, positions):
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
            new_cost = dist[node] + w

            if new_cost < dist.get(neigh, float("inf")):
                dist[neigh] = new_cost
                prev[neigh] = node

                h = graph.heuristic_euclidean(neigh, goal, positions)
                heapq.heappush(pq, (new_cost + h, neigh))

    t1 = time.time()

    return {
        "cost": dist.get(goal, float("inf")),
        "visited": visited,
        "time": t1 - t0
    }
