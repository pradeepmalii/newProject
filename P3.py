# 3 Implement Cristian’s or Berkeley’s algorithm in a simulated distributed environment.

import time
import random


# -------------------------
# Time Server
# -------------------------
class TimeServer:

    def get_time(self):

        # Return current server time
        return time.time()


# -------------------------
# Client Node
# -------------------------
class Client:

    def __init__(self, clock_offset):

        # Client clock ahead/behind by offset seconds
        self.clock_offset = clock_offset

    # Get client local time
    def get_local_time(self):

        return time.time() + self.clock_offset

    # Cristian's Algorithm
    def synchronize_clock(self, server):

        print("\n--- Cristian's Algorithm ---")

        # Client sends request at time T1
        T1 = self.get_local_time()

        print("Client sends request at:", T1)

        # Simulated network delay
        delay = random.uniform(0.1, 0.5)

        time.sleep(delay)

        # Server sends current time
        server_time = server.get_time()

        # Simulated return delay
        time.sleep(delay)

        # Client receives response at time T2
        T2 = self.get_local_time()

        print("Client receives response at:", T2)

        # Round Trip Time
        RTT = T2 - T1

        print("Estimated RTT:", RTT)

        # Cristian's adjusted time
        adjusted_time = server_time + (RTT / 2)

        # Adjust client clock
        self.clock_offset = adjusted_time - time.time()

        print("\nClient clock synchronized!")

        print("New Client Time:", self.get_local_time())


# -------------------------
# Main Program
# -------------------------
if __name__ == "__main__":

    server = TimeServer()

    # Client clock is 5 seconds slow
    client = Client(clock_offset=-5)

    print("Initial Client Time:", client.get_local_time())

    print("Server Time:", server.get_time())

    # Synchronize Client Clock
    client.synchronize_clock(server)