import heapq
import time

def dijkstra(graph, start, goal):
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

        for neighbor, weight in graph.neighbors(node):
            new_cost = cost + weight
            if new_cost < dist.get(neighbor, float("inf")):
                dist[neighbor] = new_cost
                prev[neighbor] = node
                heapq.heappush(pq, (new_cost, neighbor))

    t1 = time.time()

    return {
        "cost": dist.get(goal, float("inf")),
        "visited": visited,
        "time": t1 - t0
    }
