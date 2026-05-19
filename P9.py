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