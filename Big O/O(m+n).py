import time

list1 = ['nemo' for m in range(100000)]
list2 = ['nemo' for n in range(100000)]


def find_nemo(array1, array2):

    t0 = time.time()                # O(1)
    for i in range(0,len(array1)):  # O(m)
        if array1[i] == 'nemo':
            print("Found Nemo!!")
    t1 = time.time()                # O(1)
    print(f'The search took {t1-t0} seconds.')  # O(1)

    t0 = time.time()                 # O(1)
    for i in range(0, len(array2)):  # O(n)
        if array2[i] == 'nemo':
            print("Found Nemo!!")
    t1 = time.time()                 # O(1)
    print(f'The search took {t1 - t0} seconds.')  # O(1)


find_nemo(list1, list2)

# Here there are two different inputs array1 and array2, which could be of two different sizes m and n,
# hence you can't call it 2n instead it's O(m +n)

