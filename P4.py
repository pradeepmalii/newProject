class BullyElection:
    def __init__(self, processes):
        self.processes = processes
        self.coordinator = None

    def start_election(self, initiator):
        print(f"\nProcess {initiator} starts Bully Election")
        active_higher = False

        for pid in self.processes:
            if pid > initiator and self.processes[pid]:
                print(f"Process {initiator} sends ELECTION to {pid}")
                active_higher = True

        if not active_higher:
            self.coordinator = initiator
        else:
            self.coordinator = max(pid for pid in self.processes if self.processes[pid])

        print(f"Process {self.coordinator} becomes the COORDINATOR")

    def display(self):
        print("\nProcess Status:")
        for pid, status in self.processes.items():
            print(f"Process {pid}: {'Active' if status else 'Down'}")
        print(f"Coordinator: {self.coordinator}")


class RingElection:
    def __init__(self, processes):
        self.processes = processes
        self.coordinator = None

    def start_election(self, initiator):
        print(f"\nProcess {initiator} starts Ring Election")
        message = []
        pids = list(self.processes.keys())
        n = len(pids)
        index = pids.index(initiator)

        current = index
        while True:
            pid = pids[current]
            if self.processes[pid]:
                print(f"Process {pid} passes message")
                message.append(pid)

            current = (current + 1) % n
            if pids[current] == initiator:
                break

        self.coordinator = max(message)
        print(f"Process {self.coordinator} becomes the COORDINATOR")

    def display(self):
        print("\nProcess Status:")
        for pid, status in self.processes.items():
            print(f"Process {pid}: {'Active' if status else 'Down'}")
        print(f"Coordinator: {self.coordinator}")


def main():
    processes = {
        1: True,
        2: True,
        3: False,
        4: True,
        5: True
    }

    bully = BullyElection(processes)
    ring = RingElection(processes)

    while True:
        print("\nLEADER ELECTION MENU")
        print("1. Bully Election Algorithm")
        print("2. Ring Election Algorithm")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            bully.display()
            initiator = int(input("Enter initiator process ID: "))
            bully.start_election(initiator)

        elif choice == 2:
            ring.display()
            initiator = int(input("Enter initiator process ID: "))
            ring.start_election(initiator)

        elif choice == 3:
            print("Exiting Program...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()




# 1. Difference between Bully and Ring Election Algorithm:
# In the Bully algorithm, processes with higher IDs take priority and can replace lower-ID
# processes to become the coordinator. In the Ring algorithm, processes are arranged in a logical
# ring and election messages pass around the ring until the highest-ID process is selected. Bully
# uses direct communication, while Ring uses sequential message passing.
# 2. What is Deadlock?
# Deadlock is a situation where two or more processes wait indefinitely for resources held by each
# other. Because each process is waiting for another to release a resource, none of them can
# proceed. This causes the system to stop progressing.
# 3. What is the need of a Coordinator?
# A coordinator is needed in distributed systems to manage tasks and control access to shared
# resources. It helps coordinate communication between processes and maintains system order.
# The coordinator ensures efficient operation and synchronization among processes.
