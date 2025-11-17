from collections import deque, defaultdict

# Sample graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['H'],
    'H': ['G']
}

def bfs_path_exists(graph, start, target):
    
    if start == target:
        return True
    
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current_node = queue.popleft()
        
        # Check all neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor == target:
                return True
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False

def dfs_path_exists(graph, start, target):
    
    if start == target:
        return True
    
    visited = set()
    stack = [start]
    visited.add(start)
    
    while stack:
        current_node = stack.pop()
        
        # Check all neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor == target:
                return True
            
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    
    return False

def bfs_find_path(graph, start, target):
    
    if start == target:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])  # (node, path)
    visited.add(start)
    
    while queue:
        current_node, path = queue.popleft()
        
        for neighbor in graph.get(current_node, []):
            if neighbor == target:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []

def dfs_find_path(graph, start, target):
    
    visited = set()
    stack = [(start, [start])]  # (node, path)
    visited.add(start)
    
    while stack:
        current_node, path = stack.pop()
        
        for neighbor in graph.get(current_node, []):
            if neighbor == target:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
    
    return []

# Test all implementations
def test_solutions():
    test_cases = [
        ('A', 'F', True),   # Connected
        ('A', 'G', False),  # Not connected
        ('B', 'C', True),   # Connected through A
        ('D', 'F', True),   # Connected through B, E
    ]
    
    algorithms = {
        "BFS": bfs_path_exists,
        "DFS": dfs_path_exists,
    }
    
    for algo_name, algo_func in algorithms.items():
        print(f"\n{algo_name} Results:")
        for start, target, expected in test_cases:
            result = algo_func(graph, start, target)
            status = "✓" if result == expected else "✗"
            print(f"  {start} -> {target}: {result} {status}")

# Run tests
test_solutions()

# Test path reconstruction
print("\nPath Reconstruction:")
print(f"BFS Path A -> F: {bfs_find_path(graph, 'A', 'F')}")
print(f"DFS Path A -> F: {dfs_find_path(graph, 'A', 'F')}")
print(f"BFS Path A -> G: {bfs_find_path(graph, 'A', 'G')}")