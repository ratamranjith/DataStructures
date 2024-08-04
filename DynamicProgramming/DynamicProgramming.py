"""
    Dynamic programming

Explanation:
- The idea is to use a 2D table to store the results of subproblems. 
- The table will have a row for each element in the array and a column for each possible sum. 
- The cell at row i and column j will store the minimum number of operations  required to get 
a sum of j using the first i elements of the array.

Steps:
1. Create a 2D table with rows equal to the number of elements in the array
and columns equal to the maximum possible sum plus one.
2. Initialize the first row of the table to zero, since we can get a sum of
zero using no elements.
3. Iterate over the rows of the table. For each row, iterate over the columns.
"""


# Bottom Up approach
def fibonacci_dyn(position):

    dynamicList = [0] * position  # list Allocated
    dynamicList[0] = 1
    dynamicList[1] = 1

    # Iterate using the ranges
    for pos in range(2, position):
        dynamicList[pos] = dynamicList[pos - 1] + dynamicList[pos - 2]

    return dynamicList[position - 1]


print(fibonacci_dyn(9))
