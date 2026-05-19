# 5 Implement Ricart-Agrawala or Lamport’s algorithm.


import heapq


class Process:

    def __init__(self, pid):

        self.pid = pid
        self.clock = 0
        self.queue = []

    # Request Critical Section
    def request_cs(self):

        self.clock += 1

        timestamp = self.clock

        request = (timestamp, self.pid)

        heapq.heappush(self.queue, request)

        print(f"Process {self.pid} requests CS at time {timestamp}")

        return request

    # Receive Request
    def receive_request(self, request):

        heapq.heappush(self.queue, request)

        self.clock = max(self.clock, request[0]) + 1

    # Release Critical Section
    def release_cs(self):

        removed = heapq.heappop(self.queue)

        print(f"Process {self.pid} releases CS")

        return removed

    # Remove released request from queue
    def remove_request(self, request):

        if request in self.queue:

            self.queue.remove(request)

            heapq.heapify(self.queue)

    # Check if process can enter CS
    def can_enter_cs(self):

        return self.queue[0][1] == self.pid


# Create Processes
p1 = Process(1)
p2 = Process(2)
p3 = Process(3)

processes = [p1, p2, p3]

# Process 1 request
req1 = p1.request_cs()

for p in processes:
    if p != p1:
        p.receive_request(req1)

# Process 2 request
req2 = p2.request_cs()

for p in processes:
    if p != p2:
        p.receive_request(req2)

# Process 3 request
req3 = p3.request_cs()

for p in processes:
    if p != p3:
        p.receive_request(req3)

# Process 1 enters CS
if p1.can_enter_cs():

    print("Process 1 enters Critical Section")

    removed = p1.release_cs()

    for p in processes:
        p.remove_request(removed)

# Process 2 enters CS
if p2.can_enter_cs():

    print("Process 2 enters Critical Section")

    removed = p2.release_cs()

    for p in processes:
        p.remove_request(removed)

# Process 3 enters CS
if p3.can_enter_cs():

    print("Process 3 enters Critical Section")

    removed = p3.release_cs()

    for p in processes:
        p.remove_request(removed)