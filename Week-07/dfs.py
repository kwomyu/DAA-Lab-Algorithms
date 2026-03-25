def traverse_dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    # Action: Print or process the node
    print(f"Visiting node: {start_node}")
    
    # Mark as visited
    visited.add(start_node)
    
    # Explore all neighbors
    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            traverse_dfs(graph, neighbor, visited)

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

traverse_dfs(graph, 'A')
