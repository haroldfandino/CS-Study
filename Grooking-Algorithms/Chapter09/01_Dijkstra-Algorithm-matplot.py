import networkx as nx
import matplotlib.pyplot as plt

# This is your graph
graph = {
    'A': {'B': 5, 'E': 2},
    'B': {'C': 4, 'F': 2},
    'C': {'D': 3, 'F': 6},
    'D': {},
    'E': {'B': 8, 'F': 7},
    'F': {'D': 1}
}

# Create a directed graph in NetworkX
G = nx.DiGraph()

# Add edges from the graph with weights
for source, edges in graph.items():
    for target, weight in edges.items():
        G.add_edge(source, target, weight=weight)

# Find shortest path and distance using Dijkstra's algorithm
source_node = 'A'
destination_node = 'D'
shortest_path = nx.dijkstra_path(G, source_node, destination_node)
path_length = nx.dijkstra_path_length(G, source_node, destination_node)

# Print the shortest path and total distance
print(f"Shortest path from {source_node} to {destination_node}: {' -> '.join(shortest_path)}")
print(f"Total distance: {path_length}")

# Print all edges and weights in the graph
print("\nAll edges and weights in the graph:")
for edge in G.edges(data=True):
    print(f"From {edge[0]} to {edge[1]}: weight = {edge[2]['weight']}")

# Visualization of the graph
pos = nx.spring_layout(G)  # Define layout for graph

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_size=500, node_color="lightblue")
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color="gray", arrows=True)

# Highlight the shortest path
shortest_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=shortest_edges, edge_color="red", width=2, arrows=True)

# Add edge labels for weights
edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Display the graph
plt.title(f"Graph with Shortest Path Highlighted: {source_node} to {destination_node}")
plt.show()