#
# * String 01 Strings: Making Anagrams
# * Easy

# * Alice is taking a cryptography class and finding anagrams to be very useful. 
# * We consider two strings to be anagrams of each other if the first string's 
# * letters can be rearranged to form the second string. In other words, both 
# * strings must contain the same exact letters in the same exact frequency For 
# * example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

# * Alice decides on an encryption scheme involving two large strings where 
# * encryption is dependent on the minimum number of character deletions required 
# * to make the two strings anagrams. Can you help her find this number?

# * Given two strings, a and b, that may or may not be of the same length, determine 
# * the minimum number of character deletions required to make a and b anagrams. 
# * Any characters can be deleted from either of the strings.

# * For example, if a=ade and b=dcf, we can delete e from string a and f from 
# * string b so that both remaining strings are cd and dc which are anagrams.

# * Function Description

# Complete the makeAnagram function in the editor below. It must return an integer 
# representing the minimum total characters that must be deleted to make the 
# strings anagrams.

# makeAnagram has the following parameter(s):

#     a: a string
#     b: a string

# * Input Format

# The first line contains a single string, a.
# The second line contains a single string, b.

# * Constraints

# 1 <= |a|, |b| <= 1e4
# The strings a and b consist of lowercase English alphabetic letters ascii[a-z].

# * Output Format

# Print a single integer denoting the number of characters you must delete to make 
# the two strings anagrams of each other.

# * Sample Input

# cde
# abc

# * Sample Output

# 4

# * Explanation

# We delete the following characters from our two strings to turn them into anagrams of each other:

#     Remove d and e from cde to get c.
#     Remove a and b from abc to get c.

# We must delete 4 characters to make both strings anagrams, so we print 4 on a 
# new line.

#%%

# * Solution 1
def makeAnagram1(a: str, b: str)-> int :
    common1 = {}
    for char in a:
        if char in b:
            if char in common1:
                common1[char] +=1
            else:
                common1[char] = 1
    
    uncommonSize1 = len(a) - sum(v for v in common1.values())
    print(common1)
    print(len(a))
    print(uncommonSize1)

    common2 = {}
    for char in b:
        if char in a:
            if char in common2:
                common2[char] +=1
            else:
                common2[char] = 1

    uncommonSize2 = len(b) - sum(v for v in common2.values())
    print(common2)
    print(len(b))
    print(uncommonSize2)

    commonSizeDiff = 0
    for k, v in common1.items():
        commonSizeDiff += abs(v - common2[k])

    return uncommonSize1 + uncommonSize2 + commonSizeDiff


# * Solution 2
from collections import Counter

# ! Counter, and Counter.subtract()
def makeAnagram2(a: str, b: str)-> int :
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())


a1 = 'cde'
b1 = 'abc'
e1 = 4
r1 = makeAnagram2(a1, b1)
print('For {}, {}, expected: {}, result: {}'.format(a1, b1, e1, r1))

a2 = 'fcrxzwscanmligyxyvym'
# print(len(a2))
b2 = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
# print(len(b2))
e2 = 30
r2 = makeAnagram2(a2, b2)
print('For {}, {}, expected: {}, result: {}'.format(a2, b2, e2, r2))

# %%
