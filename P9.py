# 9 Fault Tolerance Mechanisms
import random

file = "log.txt"


try:
    f = open(file, "r")
    last = int(f.read())
    f.close()
except:
    last = 0

print("Starting from step:", last)

try:
    for i in range(last + 1, 11):
        print("Step:", i)

        
        f = open(file, "w")
        f.write(str(i))
        f.close()

    
        if random.random() < 0.3:
            raise Exception("Crash")

except:
    print("Failure! Restart program to recover.")



#     1. Write Short note on Checkpoint?
# Checkpointing is a fault tolerance technique used in distributed systems where the current state of a process is
# periodically saved to stable storage. In case of a failure, the system can restart from the last saved checkpoint
# instead of beginning from scratch. This helps in minimizing computation loss and recovery time.
# 2. Explain Fault Tolerance Mechanisms?
# Fault tolerance mechanisms are techniques used to ensure that a system continues to operate properly
# even in the presence of failures. These include:
#  Checkpointing and Recovery – Saving system state and resuming after failure
#  Replication – Duplicating components or data across multiple nodes
#  Redundancy – Having backup systems or resources
#  Error Detection and Correction – Identifying and fixing errors automatically
# 3. What is rollback?
# Rollback is the process of reverting a system to a previously saved checkpoint after a failure occurs.
# Instead of continuing from the point of failure, the system goes back to the last consistent state and
# resumes execution from there. This ensures correctness and consistency in distributed systems. 