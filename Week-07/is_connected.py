from collections import deque

def is_connected(graph, source, destination):
    # If source and destination are the same, they are connected
    if source == destination:
        return True
    
    # Track visited nodes to avoid infinite loops (cycles)
    visited = {source}
    # Queue for BFS
    queue = deque([source])
    
    while queue:
        current_node = queue.popleft()
        
        # Check all neighbors of the current node
        for neighbor in graph.get(current_node, []):
            if neighbor == destination:
                return True
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return False

# Example Usage:
# Representing the graph as an adjacency list
network = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(f"Is A connected to F? {is_connected(network, 'A', 'F')}") # True
print(f"Is B connected to E? {is_connected(network, 'B', 'E')}") # False
