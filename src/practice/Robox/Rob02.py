#%%

def compressWord(word: str, k:int)->str:
    newWord = word
    found = False
    for i in range(len(word)):
        # print(word[i])
        search = word[i]*k
        # print(search)
        while(search in newWord):
            found = True
            newWord = newWord.replace(search,'')

    if found:
        compressWord(newWord, k)

    return newWord



s1 = 'abbcccb'
print('For ', s1)
print(compressWord(s1, 3))


# %%
