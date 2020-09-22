#
# * Array 03. New Year Chaos
# * Medium

# * It's New Year's Day and everyone's in line for the Wonderland rollercoaster 
# * ride! There are a number of people queued up, and each person wears a sticker 
# * indicating their initial position in the queue. Initial positions increment 
# * by 1 from 1 at the front of the line to n at the back.

# Any person in the queue can bribe the person directly in front of them to swap 
# positions. If two people swap positions, they still wear the same sticker 
# denoting their original places in line. One person can bribe at most two others. 
# For example, if n = 8 and Person 5 bribes Person 4, the queue will look like 
# this: 1,2,3,5,4,6,7,8.

# Fascinated by this chaotic queue, you decide you must know the minimum number 
# of bribes that took place to get the queue into its current state!

# * Function Description

# Complete the function minimumBribes in the editor below. It must print an integer 
# representing the minimum number of bribes necessary, or Too chaotic if the line 
# configuration is not possible.

# minimumBribes has the following parameter(s):

#     q: an array of integers

# * Input Format

# The first line contains an integer t, the number of test cases.

# Each of the next t pairs of lines are as follows:
# - The first line contains an integer t, the number of people in the queue
# - The second line has n space-separated integers describing the final state of 
# the queue.

# * Constraints

# 1 <= t <= 10
# 1 <= n <= 1e5

# Subtasks

# For 60% score 1<= n <= 1000
# For 100% score 1 <= n <= 1e5

# * Output Format

# Print an integer denoting the minimum number of bribes needed to get the queue 
# into its final state. Print Too chaotic if the state is invalid, i.e. it requires 
# a person to have bribed more than 2 people.

# * Sample Input

# 2
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4

# Sample Output

# 3
# Too chaotic


#%%
# ! Not fully solved, all methods are time out for huge array

# * Solution 1
# ! Idea:
# ? For the number q[i] at each index i, check how many numbers (subSum) smaller 
# ? than q[i] after index i. subSum is the number of exchanges.
def minimumBribes(q: list, t: int)-> int:
    sum = 0;
    n = len(q)
    for i in range(n):
        x = q[i]
        subSum = 0
        for j in range(i+1, n):
            y = q[j]
            if (x > y):
                sum += 1
                subSum += 1
            if subSum > t:
                return -1

    return sum


# * Solution 2
def minimumBribes2(q: list, t: int)-> int:
    sum = 0;
    n = len(q)
    for i in range(n):
        x = q[i]
        if (x - i - 1) > t:
            return -1
        for j in range(i+1, n):
            y = q[j]
            if (x > y):
                sum += 1

    return sum


# * Solution 3
def minimumBribes3(q: list, t: int)-> int:
    sum = 0;
    n = len(q)
    for i in range(n):
        x = q[i]
        if (x - i - 1) > t:
            return -1

        temp = q[i+1:n]
        temp.sort()
        found = False
        for j in range(n-i-1):
            y = temp[j]
            if(y > x):
                sum += j;
                found = True
                break;

        if not found:
            sum+= (n-i-1)

    return sum



q1 = [2, 1, 5, 3, 4]
r1 = minimumBribes3(q1, 2)
print('For {}, expected: {}, result: {}'.format(q1, 3, r1))

q2 = [2, 5, 1, 3, 4]
r2 = minimumBribes3(q2, 2)
print('For {}, expected: {}, result: {}'.format(q2, -1, r2))

q3 = [1, 2, 5, 3, 7, 8, 6, 4]
r3 = minimumBribes3(q3, 2)
print('For {}, expected: {}, result: {}'.format(q3, 7, r3))

q4 = [1, 2, 5, 3, 4, 7, 8, 6]
r4 = minimumBribes3(q4, 1)
print('For {}, expected: {}, result: {}'.format(q4, 4, r4))

