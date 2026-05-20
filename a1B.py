# Depth First Search (DFS) algorithm for graph traversal.

def dfs(graph, node, visited=None):

    if visited is None:
        visited = set()

    if node not in visited:
        print(node)

        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Calling DFS function
dfs(graph, 'A')