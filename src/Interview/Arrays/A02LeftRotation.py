#
#  * Array 02 Left Rotation
#  * Easy
 
#  * A left rotation operation on an array shifts each of the array's elements 1 
#  * unit to the left. 
#  * For example, if left rotations are performed on array [1, 2, 3, 4, 5], then 
#  * the array would become [3, 4, 5, 1, 2].

#  * Given an array a of n integers and a number, d, perform d left rotations on 
#  * the array. Return the updated array to be printed as a single line of space-
#  * separated integers.


#  * Function Description

# Complete the function rotLeft in the editor below. It should return the resulting 
# array of integers.

# rotLeft has the following parameter(s):

#     An array of integers a.
#     An integer d, the number of rotations.

#  * Input Format

# The first line contains two space-separated integers n and d, the size of a and 
# the number of left rotations you must perform.
# The second line contains n space-separated integers a[i].

#  * Constraints
 
#  1 <= n <= 1e5
#  1 <= d <= n
#  1 <= a[i] <= 1e6

#  * Output Format

# Print a single line of n space-separated integers denoting the final state of the 
# array after performing d left rotations.

#  * Sample Input

# 5 4
# 1 2 3 4 5

#  * Sample Output

# 5 1 2 3 4

# Explanation

# When we perform

# left rotations, the array undergoes the following sequence of changes:

#%%
def rotLeft(a: list, d: int)-> int:
    n = len(a)
    result = [0] * n
    for i in range(n):
        result[i] = a[(i+d)%n]

    return result


def rotLeft1(a: list, d: int)-> int:
    n = len(a)
    return a[d:] + a[:d]


a1 = [1, 2, 3, 4, 5]
r1 = rotLeft(a1, 4)
print(r1)

r2 = rotLeft1(a1, 4)
print(r2)


# %%
