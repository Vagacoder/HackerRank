#%%
def prison(n, m, h, v):
    def widestGap(a:list)-> int:
        n = len(a)    
        result = 0
        curSum = 0
        for i in range(1, n):
            if a[i] != a[i-1] + 1:
                if curSum > result:
                    result = curSum
                curSum = 0
            else:
                curSum += 1
        if curSum > result:
            result = curSum
        return result

    hgap = widestGap(h)+2
    vgap = widestGap(v)+2

    return hgap * vgap



n = 3
m = 3
h = [2]
v = [2]
r1 = prison(n, m, h,v)
print(r1)

n = 3
m = 2
h = [1, 2, 3]
v = [1, 2]
r1 = prison(n, m, h,v)
print(r1)
