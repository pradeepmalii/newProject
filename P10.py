# practical 10 
def local_wc():
    try:
        text = open("input.txt", "r").read().lower().split()

        print("\nLocal Result:")

        for w in set(text):
            print(w, ":", text.count(w))

    except FileNotFoundError:
        print("input.txt not found!")


def spark_wc():
    try:
        from pyspark import SparkContext

        sc = SparkContext("local[*]", "WordCount")

        r = (
            sc.textFile("input.txt")
            .flatMap(lambda x: x.split())
            .map(lambda x: (x.lower(), 1))
            .reduceByKey(lambda a, b: a + b)
            .collect()
        )

        print("\nPySpark Result:")

        for w, c in r:
            print(w, ":", c)

        sc.stop()

    except ImportError:
        print("PySpark not installed!")

    except Exception as e:
        print("Error:", e)


ch = input("1. Local  2. PySpark : ")

if ch == "1":
    local_wc()

elif ch == "2":
    spark_wc()

else:
    print("Invalid Choice!")






#     1. Write a short note on pyspark?
# PySpark is the Python API for Apache Spark, an open-source distributed computing framework. It allows users
# to process large-scale data using Python with high speed and efficiency. PySpark supports in-memory
# computation, making it faster than traditional disk-based systems. It is widely used for big data processing,
# machine learning, and real-time analytics.

# 2. Explain hadoop?
# Apache Hadoop is an open-source framework used for storing and processing large datasets across
# clusters of computers. It consists of two main components:
#  HDFS (Hadoop Distributed File System): Stores large data across multiple machines
#  MapReduce: Processes data in parallel 

# What difference between pyspark and hadoop?
# Feature PySpark Hadoop
# Processing Speed Faster (in-memory processing)     Slower (disk-based processing)
# Ease of Use Easy (Python support)     More complex (Java-based)
# Framework Type Data processing engine       Storage + processing framework
# Real-time Processing      Supported Limited
# API High-level APIs        Low-level MapReduce 