def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ") 
            
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return visited


def dfs_recursive(graph, node, visited=None):
    
    if visited is None:
        visited = set()
    
    if node not in visited:
        visited.add(node)
        print(node, end=" ")  
        
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)
    
    return visited




# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Iterative DFS:")
dfs_iterative(graph, 'A')  # Output: A C F B E D

print("\nRecursive DFS:")
dfs_recursive(graph, 'A')  # Output: A B D E F C