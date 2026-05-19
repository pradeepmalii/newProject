#6 parallel matrix multiplication using OpenMP or MPI

import multiprocessing
import time


SIZE = 3


A = [[i + j for j in range(SIZE)] for i in range(SIZE)]

B = [[i * j for j in range(SIZE)] for i in range(SIZE)]


def multiply_row(i):

    row = []

    for j in range(SIZE):

        sum_val = 0

        for k in range(SIZE):

            sum_val += A[i][k] * B[k][j]

        row.append(sum_val)

    return row


if __name__ == "__main__":

    
    start_seq = time.time()

    seq_result = []

    for i in range(SIZE):
        seq_result.append(multiply_row(i))

    end_seq = time.time()

    print("\nSequential Time:", end_seq - start_seq, "seconds")

    print("\nMatrix A:")
    for row in A:
        print(row)

    print("\nMatrix B:")
    for row in B:
        print(row)

    print("\nSequential Result Matrix:")
    for row in seq_result:
        print(row)

    
    start = time.time()

    
    with multiprocessing.Pool() as pool:
        result = pool.map(multiply_row, range(SIZE))

    end = time.time()

    print("\nParallel Result Matrix C:")
    for row in result:
        print(row)

    print("\nParallel Time Taken:", end - start, "seconds")



#     1. What is the use of shared memory?
# Shared memory is a memory management technique that allows multiple processes or threads to
# access a common memory space for communication and data exchange. It allows fast and
# efficient interaction between processes without the overhead of sending messages over a network.
# 2. What do you mean by MPI?
# MPI, or Message Passing Interface, is a standardized library used for communication in
# distributed computing systems. It allows processes running on different machines or nodes to
# exchange data through message passing, enabling coordination and synchronization in parallel
# applications.
# 3. What is difference between distributed and shared memory?
# Distributed memory and shared memory are two approaches to process communication in parallel
# computing. In distributed memory systems, each process has its own private memory, and
# processes communicate by sending and receiving messages, as in MPI. In shared memory
# systems, multiple processes access a common memory space directly, allowing fast data sharing
# without message passing.
