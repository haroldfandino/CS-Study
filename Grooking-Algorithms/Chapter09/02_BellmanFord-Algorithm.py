class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, source, destination, weight):
        if source not in self.graph:
            self.graph[source] = {}
        self.graph[source][destination] = weight
    
    def get_vertices(self):
        vertices = set(self.graph.keys())
        for node in self.graph:
            vertices.update(self.graph[node].keys())
        return vertices

def bellman_ford(graph, start):
    """
    Implements Bellman-Ford algorithm for shortest paths with negative weights
    
    Args:
        graph: Graph object containing the adjacency list
        start: Starting vertex
    
    Returns:
        tuple: (distances dictionary, parents dictionary) or (None, None) if negative cycle exists
    """
    # Initialize distances dictionary
    vertices = graph.get_vertices()
    distances = {node: float('inf') for node in vertices}
    distances[start] = 0
    
    # Initialize parent dictionary to track the shortest path
    parents = {node: None for node in vertices}
    
    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for node in graph.graph:
            for neighbor, weight in graph.graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    parents[neighbor] = node
    
    # Check for negative weight cycles
    for node in graph.graph:
        for neighbor, weight in graph.graph[node].items():
            if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                print("Warning: Graph contains a negative weight cycle")
                return None, None
                
    return distances, parents

def get_shortest_path(parents, start, destination):
    """
    Reconstructs the shortest path from start to destination
    
    Args:
        parents: Dictionary of parent nodes
        start: Starting vertex
        destination: Destination vertex
    
    Returns:
        list: Path from start to destination, or empty list if no path exists
    """
    if destination not in parents:
        print(f"Error: Destination node {destination} not found in graph")
        return []
        
    path = []
    current_node = destination
    
    while current_node is not None:
        path.insert(0, current_node)
        current_node = parents[current_node]
        
        # Check for infinite loop
        if len(path) > len(parents):
            print(f"Error: Cycle detected in path reconstruction")
            return []
    
    if not path or path[0] != start:
        print(f"No path exists from {start} to {destination}")
        return []
        
    return path

def print_result(distances, path, start, destination):
    """Prints the results in a formatted way"""
    if path:
        print(f"\nShortest path from {start} to {destination}: {' -> '.join(path)}")
        print(f"Total distance: {distances[destination]}")
    print("\nDistances from source:")
    for vertex, distance in sorted(distances.items()):
        print(f"{vertex}: {distance}")

def main():
    # Example usage
    g = Graph()
    
    # Add edges to the graph
    edges = [
        ('A', 'B', 2), ('A', 'D', 2),
        ('B', 'C', 2), ('B', 'E', 2),
        ('D', 'B', 2),
        ('E', 'D', -1), ('E', 'C', 2)
    ]
    
    for source, dest, weight in edges:
        g.add_edge(source, dest, weight)
    
    # Run algorithm
    start_node = 'A'
    end_node = 'C'
    
    distances, parents = bellman_ford(g, start_node)
    
    if distances:
        path = get_shortest_path(parents, start_node, end_node)
        print_result(distances, path, start_node, end_node)

if __name__ == "__main__":
    main()