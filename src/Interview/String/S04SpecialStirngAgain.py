#
# * String 04. Special String Again

# * A string is said to be a special string if either of two conditions is met:

#     All of the characters are the same, e.g. aaa.
#     All characters except the middle one are the same, e.g. aadaa.

# * A special substring is any substring of a string which meets one of those 
# * criteria. Given a string, determine how many special substrings can be formed 
# * from it.

# * For example, given the string s = mnonopoo, we have the following special substrings:
# * {m, n, o, n, o, p, o, o, non, ono, opo, oo}.

# * Function Description

# * Complete the substrCount function in the editor below. It should return an 
# * integer representing the number of special substrings that can be formed from 
# * the given string.

# * substrCount has the following parameter(s):

#     n: an integer, the length of string s
#     s: a string

# * Input Format

# The first line contains an integer, n, the length of s.
# The second line contains the string s.

# * Constraints

# 1 <= n <= 1e6

# Each character of the string is a lowercase alphabet ascii[a-z].

# * Output Format

# Print a single line containing the count of total special substrings.

# * Sample Input 0

# 5
# asasd

# * Sample Output 0

# 7 

# * Explanation 0

# The special palindromic substrings of s=asasd are {a, s, a, s ,d ,asa, sas}

# * Sample Input 1

# 7
# abcbaba

# Sample Output 1

# 10 

# Explanation 1

# The special palindromic substrings of s=abcbaba are {a, b, c, b, a, b, a, bcb, bab, aba}

# * Sample Input 2

# 4
# aaaa

# Sample Output 2

# 10

# Explanation 2

# The special palindromic substrings of s= aaaa are {a, a, a, a, aa, aa, aa, aaa, aaa, aaaa}

#%%

# ! Timeout
# * Solution 1
# ? brute force
def substrCount1(n: int, s:str) -> int:
    count = n

    for size in range(2, n+1):
        for i in range(n-size+1):
            if isSpecial(s[i:i+size]):
                count+=1

    return count


def isSpecial(s:str)-> bool:
    n = len(s)
    c1 = s[0]
    for i, c in enumerate(s):
        if i == (n-1)//2  and n%2 == 1:
            continue
        if c != c1:
            return False

    return True

    
# * Solution 2
# ! Idea:
# ? Two pointer, i from 0 to n, j from i
# ? j does 2 jobs:
# ? (1) find type 1 string (aaaaa), j stops at 1) end of string,
# ?     2) the middle one (b) of type 2 string (aabaa).
# ? (2) find second half of type 2 string (aabaa).
# !     Note: second half of type 2 is a type 1, but length must <= first half 
def substrCount2(n: int, s:str) -> int:
    count = 0
    i = 0

    while i < n:
        j = i+1

        # ! find type 1 special string (aaaaa)
        while j < n and s[j]==s[i]:
            j+=1
        
        # * length of type 1 / first half of type 2
        length = j-i
        # ! calculate numbers of all possible type 1 special string
        count += ((1+length)*length//2)

        # ! save index of middle index of potential type 2 special string (aba)
        k = j
        # ! find second half type 2 special string (aabaa)
        j += 1
        # ! Note condition of j-k-1 (length) < length (1st half)
        # * This ensure second half <= first half
        while j < n and j-k-1 < length and s[j] == s[i]:
            j+=1
        
        length = j-k-1
        count += length

        # ! Note i move to k, since we already calculate all possible type 1 string
        # ! from i to k-1
        i = k

    return count


# * Solution 3
# ! Awesome
# ! Idea
# ? Pass 1: turn string ('aaabbaacbbbacc') to a list of tuple:
# ?     [('a',3),('b',2),('a',2),('c',1),('b',3),('a',1),('c',2)]
# ? Pass 2: calculate type 1 string for each tuple
# ? Pass 3: calculate type 2 string for whole list
def substrCount3(n, s):
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0
		
# 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

# 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans



s1 = 'aaaa'
n1 = len(s1)
e1 = 10
r1 = substrCount2(n1, s1)
print('For "{}", expected: {}, result: {}'.format(s1, e1, r1))

s2 = 'asasd'
n2 = len(s2)
e2 = 7
r2 = substrCount2(n2, s2)
print('For "{}", expected: {}, result: {}'.format(s2, e2, r2))

s2 = 'abcbaba'
n2 = len(s2)
e2 = 10
r2 = substrCount2(n2, s2)
print('For "{}", expected: {}, result: {}'.format(s2, e2, r2))

s2 = 'ooopoooooo'
n2 = len(s2)
e2 = 31
r2 = substrCount2(n2, s2)
print('For "{}", expected: {}, result: {}'.format(s2, e2, r2))

# %%
