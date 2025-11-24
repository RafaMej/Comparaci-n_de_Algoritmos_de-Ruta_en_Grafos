import random, json, os

def generate_graph(n_nodes, filename):
    positions = {i: (random.random()*100, random.random()*100) for i in range(n_nodes)}
    graph = {i: [] for i in range(n_nodes)}

    for i in range(n_nodes):
        for _ in range(random.randint(2, 5)):
            j = random.randint(0, n_nodes-1)
            if i != j:
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                w = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
                graph[i].append([j, w])

    with open(filename, "w") as f:
        json.dump({"positions": positions, "graph": graph}, f)

if __name__ == "__main__":
    generate_graph(100, "data/graphs_100.json")
    generate_graph(500, "data/graphs_500.json")
    generate_graph(1000, "data/graphs_1000.json")

