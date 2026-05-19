# 7 Use OpenMP or MPI to sort an array in parallel

from multiprocessing import Process, Queue


def merge(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def parallel_sort(arr, q):

    sorted_part = merge_sort(arr)
    q.put(sorted_part)


if __name__ == "__main__":

    arr = [8, 3, 7, 4, 9, 2, 6, 5]

    mid = len(arr) // 2

    q1 = Queue()
    q2 = Queue()

    p1 = Process(target=parallel_sort, args=(arr[:mid], q1))
    p2 = Process(target=parallel_sort, args=(arr[mid:], q2))

    p1.start()
    p2.start()

    left = q1.get()
    right = q2.get()

    p1.join()
    p2.join()

    sorted_arr = merge(left, right)

    print("Original Array:", arr)
    print("Sorted Array:", sorted_arr)                                    



#     1. What do you mean by message passing system?
# A message passing system is a communication mechanism used in parallel and distributed
# computing where processes exchange data by sending and receiving messages. Instead of sharing
# memory, processes communicate explicitly through message transfers, which ensures
# coordination and synchronization across different nodes or machines.

# 2. What is difference between OpenMP and MPI?
# OpenMP and MPI are both used for parallel computing but differ in their approach. OpenMP is
# designed for shared memory systems and uses compiler directives to create parallel threads
# within a single machine, allowing direct access to shared memory. MPI, on the other hand, is
# designed for distributed memory systems and relies on message passing to communicate between
# processes on different machines.
# 3. What is parallel merge sort?
# Parallel merge sort is a sorting algorithm that divides the data into smaller segments and sorts
# them simultaneously using multiple processors or threads. Once the segments are sorted, they are
# merged in parallel to produce the final sorted sequence. Proper use of parallel merge sort reduces
# execution time and improves efficiency for large datasets, making it suitable for highperformance computing and data-intensive applications.
