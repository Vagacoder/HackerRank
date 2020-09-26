#
# * String 03. Sherlock and the Valid String
# * Medium

# * Sherlock considers a string to be valid if all characters of the string appear 
# * the same number of times. It is also valid if he can remove just 1 character 
# * at 1 index in the string, and the remaining characters will occur the same 
# * number of times. Given a string s, determine if it is valid. If so, return 
# * YES, otherwise return NO.

# * For example, if s= abc, it is a valid string because frequencies are {a:1, 
# * b:1, c:1}. So is s=abcc because we can remove one c and have 1 of each character 
# * in the remaining string. If s=abccc however, the string is not valid as we 
# * can only remove 1 occurrence of c. That would leave character frequencies of 
# * {a:1, b:1, c:2}.

# * Function Description

# * Complete the isValid function in the editor below. It should return either 
# * the string YES or the string NO.

# isValid has the following parameter(s):

#     s: a string

# * Input Format

# A single string s.

# * Constraints

# 1 <= |s| <= 1e5
# Each character belongs to ascii[a-z]

# * Output Format

# Print YES if string s is valid, otherwise, print NO.

# * Sample Input 0

# aabbcd

# Sample Output 0

# NO

# Explanation 0

# Given s="aabbcd", we would need to remove two characters, both c and d -> aabb 
# or a and b -> abcd, to make it valid. We are limited to removing only one 
# character, so s is invalid.

# * Sample Input 1

# aabbccddeefghi

# Sample Output 1

# NO

# Explanation 1

# Frequency counts for the letters are as follows:

# {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

# There are two ways to make the valid string:

#     Remove 4 characters with a frequency of 1:{fghi}.
#     Remove 5 characters of frequency 2:{abcde}.

# Neither of these is an option.

# * Sample Input 2

# abcdefghhgfedecba

# Sample Output 2

# YES

# Explanation 2

# All characters occur twice except for e which occurs 3 times. We can delete one 
# instance of e to have a valid string.

#%%


# * Solution 1

def isValid(s:str)->str:
    # * dict1 is counting freqency of char in string
    dict1 = {}
    for c in s:
        if c in dict1:
            dict1[c]+=1
        else:
            dict1[c] = 1
    
    print(dict1)

    # * dictCount is counting frequency of frequency of char in string
    dict1Count = {}
    for v in dict1.values():
        if v in dict1Count:
            dict1Count[v] +=1
        else:
            dict1Count[v] = 1
    
    print(dict1Count)

    dict1CountSize = len(dict1Count)
    
    # * if there is only one frequency, it is always good
    if dict1CountSize == 1:
        return 'YES'
    # * if there are 2 frequencies, 
    elif dict1CountSize == 2:
        keys = [0]*2
        values = [0]*2

        # ! sort dictCount keys !
        for i, key in enumerate(sorted(dict1Count.keys())):
            keys[i] = key
            values[i] = dict1Count[key]
        print(keys)
        print(values)
        # * if none of 2 frequencies == 1
        if keys[0] > 1 and keys[1] >1:
            # * To be good, higher frequency must only 1 larger than smaller frequency
            # * And higher frequency must happend only once
            if (keys[1] - keys[0] ==1) and (values[1] == 1) :
                return 'YES'
            else:
                return 'NO'
        # * if one of 2 frequencies == 1, in this case keys[0] must be 1 (lower frequency must be 1)
        else:
            # * if lower frequency (1) happens only once, it is always good (remove it to be good)
            # * if higher frequenc is 2, and happeen only once, it is good (remove it to be good)
            if values[0] == 1 or (values[1] ==1 and keys[1] == 2) :
                return 'YES'
            else:
                return 'NO'
    # * if there are more than two frequencies, it is always bad
    else:

        return 'NO'




s1 = 'abcc'
e1 = 'YES'
r1 = isValid(s1)
print('For {}, expected: {}, result: {}'.format(s1, e1, r1))

s2 = 'aabbcd'
e2 = 'NO'
r2 = isValid(s2)
print('For {}, expected: {}, result: {}'.format(s2, e2, r2))

s3 = 'aabbccddeefghi'
e3 = 'NO'
r3 = isValid(s3)
print('For {}, expected: {}, result: {}'.format(s3, e3, r3))

s4 = 'aaaabbcc'
e4 = 'NO'
r4 = isValid(s4)
print('For {}, expected: {}, result: {}'.format(s4, e4, r4))

s5 = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
e5 = 'YES'
r5 = isValid(s5)
print('For {}, expected: {}, result: {}'.format(s5, e5, r5))

s6 = 'aaaaabc'
e6 = 'NO'
r6 = isValid(s6)
print('For {}, expected: {}, result: {}'.format(s6, e6, r6))

# %%
