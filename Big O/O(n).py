# Big O : How well a problem is solved?
# When we grow bigger and bigger with the input, how much does the algorithm fn slow down
# measurement of complexity, not always related to input
# Algorithmic efficiency ( x-axis vs y-axis / elements vs operations)
# What is a good code?
# 1. Readable
# 2. Scalable (Big O) - Run Time : How long does an algorithm takes to run


import time

single_name = ["Nemo"]
everyone = ["Nemo", "Table", "Lola", "Toy"]
small_list = ["Nemo" for i in range(10)]
medium_list = ["Nemo" for m in range(100)]
large_list = ["Nemo" for n in range(10000)]


def find_name(names):
    t0 = time.time()
    for item in names:
        if item == "Nemo":
            print("Found Nemo")
    t1 = time.time()
    print(f"Time taken is {t1 - t0}")


def funchallenge(input):
    a = 10                       # O(1)
    a = 3 +50                    # O(1)
    for i in range(len(input)):
        var = True               # O(n)
        a += 1                   # O(n)
    return a                     # O(1)


if __name__ == "__main__":
    find_name(single_name)


# Note: Loops are O(n)
# find_name has O(n) Linear Time Complexity
# n here is the number of elements, as the elements size increases linearly, it takes n operations to complete the task
# ---------------------
# Rule Book:
# 1. Worst Case
# 2. Remove Constants
# 3. Different terms for inputs (**IMP) (m and n)
# 4. Drop Non Dominants (O(n^2 + 8n + 100 + n/2) --> n^2








