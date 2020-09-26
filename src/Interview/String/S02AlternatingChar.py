#
# * String 02. Alternating Characters
# * You are given a string containing characters A and B only. Your task is to 
# * change it into a string such that there are no matching adjacent characters. 
#  * To do this, you are allowed to delete zero or more characters in the string.

# * Your task is to find the minimum number of required deletions.

# * For example, given the string s=AABAAB, remove an A at positions 0 and 3 to 
# * make s=ABAB in 2 deletions.

# * Function Description

# Complete the alternatingCharacters function in the editor below. It must return 
# an integer representing the minimum number of deletions to make the alternating 
# string.

# alternatingCharacters has the following parameter(s):

#     s: a string

# * Input Format

# The first line contains an integer q, the number of queries.
# The next q lines each contain a string s.

# * Constraints

# 1 <= q <= 10
# 1 <= |s| <=1e5
# Each string s will consist only of characters A and B

# * Output Format

# For each query, print the minimum number of deletions required on a new line.

# Sample Input

# 5
# AAAA
# BBBBB
# ABABABAB
# BABABA
# AAABBB

# Sample Output

# 3
# 4
# 0
# 0
# 4

# * Explanation

# The characters marked red are the ones that can be deleted so that the string 
# doesn't have matching consecutive characters.

# AAAA -> A (3 deletions)
# BBBBB -> B (4 deletions)
# ABABABAB -> ABABABAB (0 deletion)
# BABABA -> BABABA (0 deletion)
# AAABBB -> AB (4 deletions)

#%%

# * Solution 1
# ! Timeout
def alternatingCharacters1(s:str)->int:
    count = 0
    while 'AA' in s or 'BB' in s:
        if 'AA' in s:
            s = s.replace('AA', 'A', 1)
            count +=1
        elif 'BB' in s:
            s = s.replace('BB', 'B', 1)
            count +=1

    return count 
    
    
# * Solution 2
# ! Using regex
import re

def alternatingCharacters2(s:str)->int:
    count = 0
    while 'AA' in s or 'BB' in s:
        temp = s
        if 'AA' in s:
            s = re.sub('A+', 'A', s)
            count += (len(temp) - len(s))
        elif 'BB' in s:
            s = re.sub('B+', 'B', s)
            count += (len(temp) - len(s))

    return count 


# ! LOL, I though too much, sol1 and sol2 overkill this question
# * Solution 3
def alternatingCharacters3(s:str)->int:
    count = 0
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count+=1

    return count


s1 = 'AAAA'
e1 = 3
r1 = alternatingCharacters3(s1)
print('For {}, expected: {}, result: {}'.format(s1, e1, r1))

s2 = 'BBBBB'
e2 = 4
r2 = alternatingCharacters3(s2)
print('For {}, expected: {}, result: {}'.format(s2, e2, r2))


s3 = 'ABABAB'
e3 = 0
r3 = alternatingCharacters3(s3)
print('For {}, expected: {}, result: {}'.format(s3, e3, r3))

s4 = 'AAABBB'
e4 = 4
r4 = alternatingCharacters3(s4)
print('For {}, expected: {}, result: {}'.format(s4, e4, r4))

s5 = 'AABBAABB'
e5 = 4
r5 = alternatingCharacters3(s5)
print('For {}, expected: {}, result: {}'.format(s5, e5, r5))


# %%
