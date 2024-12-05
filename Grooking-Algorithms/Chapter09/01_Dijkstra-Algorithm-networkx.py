import networkx as nx

# This is your graph
graph = {
    'A': {'B': 5, 'E': 2},
    'B': {'C': 4, 'F': 2},
    'C': {'D': 3, 'F': 6},
    'D': {},
    'E': {'B': 8, 'F': 7},
    'F': {'D': 1}
}

# Create NetworkX graph
G = nx.DiGraph()

# Add each edge from your graph to NetworkX
for source, edges in graph.items():
    for target, weight in edges.items():
        G.add_edge(source, target, weight=weight)

# Find shortest path and distance
shortest_path = nx.dijkstra_path(G, 'A', 'D')
path_length = nx.dijkstra_path_length(G, 'A', 'D')

print(f"Shortest path from A to D: {' -> '.join(shortest_path)}")
print(f"Total distance: {path_length}")

# To verify the edges are the same as your graph, we can print them:
print("\nAll edges and weights in the graph:")
for edge in G.edges(data=True):
    print(f"From {edge[0]} to {edge[1]}: weight = {edge[2]['weight']}")