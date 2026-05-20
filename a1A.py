# Breadth First Search (BFS) algorithm for graph traversal.

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node)

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Calling BFS function
bfs(graph, 'A')



# 1.	What is BFS?  
# Ans. Breadth First Search (BFS) is an uninformed search algorithm that explores nodes level by level. It uses a queue and guarantees the shortest path when all edges have equal cost.  
 
# 2.	What is DFS?  
# Ans. Depth First Search (DFS) explores as deep as possible along a branch before backtracking. It uses a stack or recursion and is memory efficient but does not guarantee the shortest path.  
 
# 3.	Define the terms: f(n) = g(n) + h(n)  
# Ans. In A* search, g(n) is the cost from the start node to the current node. h(n) is the estimated cost to the goal, and f(n) is the total estimated cost.  
 
# 4.	Which data structure is used in DFS?  
# Ans. DFS uses a stack data structure. It can be implemented using recursion or an explicit stack.  
 
# 5.	Which algorithm finds the shortest path?  
# Ans. BFS finds the shortest path in an unweighted graph. A* finds the shortest path in weighted graphs when a valid heuristic is used. 


