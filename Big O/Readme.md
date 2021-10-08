# Big O Cheat Sheet:

1. Big O(1) Constant- no loops
2. O(log N) Logarithmic- usually searching algorithms have log n if they are sorted (Binary Search)
3. O(n) Linear- for loops, while loops through n items
4. O(n log(n)) Log Linear- usually sorting operations
5. O(n^2) Quadratic- every element in a collection needs to be compared to ever other element. Two
nested loops
6. O(2^n) Exponential- recursive algorithms that solves a problem of size N
7. O(n!) Factorial- you are adding a loop for every element

** Iterating through half a collection is still O(n)
** Two separate collections: O(a */+ b)

### What can cause time in a function?

1. Operations (+, -, *, /)
2. Comparisons (<, >, ==)
3. Looping (for, while)
4. Outside Function call (function())

### Rule Book
Rule 1: Always worst Case
Rule 2: Remove Constants
Rule 3: Different inputs should have different variables. O(a+b). 
        A and B arrays nested would be O(a*b)
        + for steps in order
        * for nested steps
Rule 4: Drop Non-dominant terms

### What causes Space complexity?
(Memory)
Variables
Data Structures
Function Call
Allocations

### Program Execution in terms of memory:
Heap: store program variables
Stack: function calls (Stack overflow)

### Ask:
Do we know any thing about the data? 
Does it have to be super efficient, we don't have infinite and money
