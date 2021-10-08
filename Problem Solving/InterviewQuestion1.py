# Problem:
# We are given two arrays, we have to find if these two arrays contain any matching elements
# Input -> 2 arrays   Output -> Bool True/False
# For example, array1 = ['a','b','c','x'] , array2 = ['x','y','z'], should return True as 'x' is present in both
# Assumptions: i/p is array, can be of different lengths, can contain repetitive values

# So, easiest approach would be brute-force solution

array1 = ['a','b','c','x']
array2 = ['x','y','z']


def brute_force_solution(array1, array2):
    for i in range(len(array1)):             # (0,4)    length m
        for j in range(len(array2)):         # (0,3)    length n
            if array1[i] == array2[j]:       # O(m*n) Quadratic complexity which you want to avoid
                return True
    return False                             # Space complexity O(1)


print(brute_force_solution(array1, array2))


# We want something less than O(N^2) or O(m*n). We want to avoid nested loops if we can since they are expensive. Two
# separate loops are better than 2 nested loops

# Better approach : Create a dictionary for one of the arrays and then loop over the other array to check if it's
# element is present in dicts keys
# Dictionaries are implemented as hash tables in python and look-up is O(1)
# Complexity = O(m + n*1) -> O(m +n), way better


def smarter_solution(array1, array2):
    dictionary = dict()
    for i in range(len(array1)):         # Using Dict comprehension {array1[i]: True for i in range(len(array1))}
        dictionary[array1[i]] = True     # {'a': True, 'b': True, 'c': True, 'x': True}    O(m)

    for j in range(len(array2)):
        if array2[j] in dictionary:      # O(n * 1)
            return True

    return False                         # Space complexity O(a) because you're creating a new dict


print(smarter_solution(array1,array2))

# Now clean up with edge cases, a. repetitive elements can be present
# b. throws error if input not array type


def smarter_solution2(array1, array2):
    try:
        dictionary = dict()
        for i in range(len(array1)):
            if array1[i] not in dictionary:      # Add only once
                dictionary[array1[i]] = True     # {'a': True, 'b': True, 'c': True, 'x': True}    O(m)

        for j in range(len(array2)):
            if array2[j] in dictionary:      # O(n * 1)
                return True
        return False

    except TypeError:
        return "Exactly two arrays required."
