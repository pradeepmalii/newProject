# Write a program to implement the A* Search Algorithm

import heapq

def a_star(graph, start, goal, heuristic):

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    visited = set()

    while open_list:

        current = heapq.heappop(open_list)[1]

        if current == goal:
            print("Goal reached:", current)
            print("Cost:", g_cost[current])
            return

        visited.add(current)

        for neighbor, cost in graph[current]:

            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                g_cost[neighbor] = new_cost

                f_cost = new_cost + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost, neighbor))

# Graph representation
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

# Heuristic values
heuristic = {
    'A': 3,
    'B': 1,
    'C': 1,
    'D': 0
}

# Calling A* function
a_star(graph, 'A', 'D', heuristic)