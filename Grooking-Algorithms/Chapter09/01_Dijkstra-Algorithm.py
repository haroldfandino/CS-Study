import heapq

#Graph for testing 1
graph = {
    'A': {'B': 5, 'E': 2},
    'B': {'C': 4, 'F': 2},
    'C': {'D': 3, 'F': 6},
    'D': {},
    'E': {'B': 8, 'F': 7},
    'F': {'D': 1}
}

#Graph for testing 2
graph2 = {
    'A': {'B': 10},
    'B': {'C': 20},
    'C': {'D': 30, 'E': 1},
    'D': {},
    'E': {'B': 1}
}

def dijkstra_with_path(graph, start, destination):
    # Priority queue to store (distance, node)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    
    # Distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Dictionary to reconstruct the shortest path
    previous_nodes = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the current node is the destination, reconstruct the path
        if current_node == destination:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return distances[destination], path[::-1]  # Reverse the path
        
        # Skip outdated distance entries
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's shorter
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node  # Track the path
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # If the destination is unreachable
    return None, []

# Set source and destination
source_node = 'A'
destination_node = 'D'

# Find the shortest distance and path
shortest_distance, path = dijkstra_with_path(graph2, source_node, destination_node)
print(f"Shortest distance from {source_node} to {destination_node}: {shortest_distance}")
print(f"Path: {' -> '.join(path)}")