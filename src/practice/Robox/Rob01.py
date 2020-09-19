
#%%
def numPlayers(k:int, scores:list)->int:
    length = len(scores)
    scores.sort(reverse=True)
    i = k
    while i < length and scores[i-1] == scores[i]:
        i+=1;

    return i


scores1 = [100, 50, 50, 25]
print(numPlayers(3, scores1))

scores2 = [0,0,0,0,0,0,0]
print(numPlayers(3, scores2))
# %%
