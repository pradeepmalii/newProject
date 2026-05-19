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