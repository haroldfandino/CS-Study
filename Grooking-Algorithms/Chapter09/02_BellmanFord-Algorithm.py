# Bellman-Ford Algorithm to handle negative weight edges

graph = {
    'A': {'B': 2, 'D': 2},
    'B': {'C': 2, 'E': 2},
    'C': {},
    'D': {'B': 2},
    'E': {'D': -1, 'C': 2},
}

def bellman_ford(graph, start):
    # Initialize distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Initialize parent dictionary to track the shortest path
    parents = {node: None for node in graph}
    
    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    parents[neighbor] = node  # Track the parent node
    
    # Check for negative weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                print("Graph contains a negative weight cycle")
                return None, None
    
    return distances, parents

def get_shortest_path(parents, start, destination):
    path = []
    current_node = destination
    
    # Backtrack to find the shortest path using the parents dictionary
    while current_node is not None:
        path.insert(0, current_node)
        current_node = parents[current_node]
    
    # If the start node isn't in the path, there is no valid path
    if path[0] != start:
        print(f"No path found from {start} to {destination}")
        return []
    
    return path

# Using Bellman-Ford algorithm
source_node = 'A'
destination_node = 'C'
distances, parents = bellman_ford(graph, source_node)

if distances:
    path = get_shortest_path(parents, source_node, destination_node)
    if path:
        print(f"Shortest path from {source_node} to {destination_node}: {path}")
    print(f"Distances from {source_node}: {distances}")