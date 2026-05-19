#8 Simulate static/dynamic load balancing 

import random

tasks = [random.randint(1, 10) for _ in range(10)]
nodes = [0, 0, 0]


for i, t in enumerate(tasks):
    nodes[i % len(nodes)] += t

print("Static Load:", nodes)


nodes = [0, 0, 0]

for t in tasks:
    idx = nodes.index(min(nodes))
    nodes[idx] += t

print("Dynamic Load:", nodes)



# 1. What is difference between static and dynamic load balancing in distributed system?
# Static and dynamic load balancing are techniques used to distribute workloads across multiple
# processors or nodes, but they differ in timing and adaptability. In static load balancing, tasks are
# assigned to nodes before execution based on predefined criteria, such as task size or node
# capacity, and do not change during runtime. Dynamic load balancing, on the other hand, monitors
# system performance and redistributes tasks during execution based on current load and resource
# availability.
# 2. How will we simulate static balancing?
# To simulate static load balancing, we assign tasks to nodes in a fixed, repeating order—usually
# using a round-robin method. Each task is added to the next node in sequence, regardless of its
# current workload. In our simulation, the tasks are numbers representing work, and nodes track
# their total load. As tasks are assigned, each node’s load increases by the task value.
# 3. How does dynamic load balancing perform in distributed system?
# Dynamic load balancing improves performance in distributed systems by continuously
# monitoring workload and reallocating tasks to underutilized nodes in real time. This approach
# reduces idle time, prevents bottlenecks, and ensures better utilization of system resources,
# especially in environments where task loads are unpredictable or vary during execution.