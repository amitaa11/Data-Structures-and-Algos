# O(1) - Constant time (Flat line)
# In this case, the no. of operations do not depend on the size of the input and are always constant


import time

single_name = ["Nemo"]
everyone = ["Nemo", "Table", "Lola", "Toy"]
small_list = ["Nemo" for i in range(10)]
medium_list = ["Nemo" for m in range(100)]
large_list = ["Nemo" for n in range(10000)]


def find_name(names):
    t0 = time.time()
    print(names[0])   # O(1)
    print(names[1])   # O(1)
    t1 = time.time()
    print(f"Time taken is {t1 - t0}")


find_name(small_list)   # O(1)
find_name(medium_list)  # O(1)
find_name(large_list)   # O(1)

# We are not looping over the entire array here and extracting a single element each time
# We are performing two O(1) operations, which equal to O(2).
# But since it's constant we can call this fn as O(1) - Constant Time Complexity.


