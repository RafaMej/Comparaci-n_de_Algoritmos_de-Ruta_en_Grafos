import json, csv, random
from src.graph import Graph
from src.dijkstra import dijkstra
from src.astar import astar
from src.uniform_cost import uniform_cost

DATASETS = [
    "../data/graphs_100.json",
    "../data/graphs_500.json",
    "../data/graphs_1000.json"
]

OUTPUT = "results.csv"

def load_graph(path):
    with open(path) as f:
        data = json.load(f)
    g = Graph()
    for u, edges in data["graph"].items():
        for v, w in edges:
            g.add_edge(int(u), int(v), float(w))
    return g, {int(k): tuple(v) for k, v in data["positions"].items()}

with open(OUTPUT, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["dataset", "start", "goal", "algo", "cost", "visited", "time"])

    for dataset in DATASETS:
        g, positions = load_graph(dataset)
        nodes = list(g.adj.keys())

        for _ in range(10):   # 10 rutas por dataset
            s, t = random.sample(nodes, 2)

            for name, fn in [
                ("Dijkstra", lambda: dijkstra(g, s, t)),
                ("A*", lambda: astar(g, s, t, positions)),
                ("Uniform Cost", lambda: uniform_cost(g, s, t))
            ]:
                result = fn()
                writer.writerow([
                    dataset, s, t, name,
                    result["cost"],
                    result["visited"],
                    result["time"]
                ])

print("Experimentos completados. Resultados guardados en", OUTPUT)
