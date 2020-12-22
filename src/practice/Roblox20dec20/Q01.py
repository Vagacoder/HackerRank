#%%
# * Solution 1
# ! Wrong idea
def minCost1(cost:list)-> int:
    n = len(cost)
    dp = cost.copy()
    
    for i in range(1, n):
        for j in range(len(cost[i])):
            prevCosts = dp[i-1][:j] + dp[i-1][j+1:]
            dp[i][j] = cost[i][j] + min(prevCosts)
    
    return min(dp[n-1])

    


c1 = [[1, 2, 2], [2, 3, 3], [3, 3, 1]]
r1 = minCost1(c1)
print(r1)

c1 = [[1, 10, 20], [2, 100, 100]]
r1 = minCost1(c1)
print(r1)
        



