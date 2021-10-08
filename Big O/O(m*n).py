
array1 = ['a','b','c','d','e']
array2 = [1,2,3,4,5]


def pairs(array1, array2):
    for i in range(len(array1)):          # n*O(m)
        for j in range(len(array2)):      # m*O(n)
            print(array1[i],array2[j])    # m*n*O(1)


pairs(array1,array2)

# Here there are two different inputs array1 and array2 (m & n) which are nested.
# Time complexity = O(m*n)

