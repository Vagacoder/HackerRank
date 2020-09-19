#%%

def largestSubgrid(grid, maxSum: int) -> int:
    n: int = len(grid)
    sizeWithMaxSum = {}

    for size in range(n):
        step = n - size + 1;
        maxCurSizeSum = 0

        for rStart in range(step):
            for cStart in range(step):
                curSizeSum = sum(grid, rStart, cStart, size)
                if curSizeSum > maxCurSizeSum :
                    maxCurSizeSum = curSizeSum

        sizeWithMaxSum[size] = maxCurSizeSum

    maxMaxSum = -1
    maxSize = -1
    for size, sizeMaxSum in sizeWithMaxSum.items():
        if sizeMaxSum <= maxSum and sizeMaxSum > maxMaxSum :
            maxMaxSum = sizeMaxSum
            maxSize = size

    return maxSize


def sum(grid, rs:int, cs:int, size:int) -> int:
    n = len(grid)
    sum = 0

    for r in range(rs, rs+size):
        for c in range(cs, cs+size):
            sum += grid[r][c]

    return sum


grid1 = [[1,1,1],[1,1,1],[1,1,1]]
print(grid1)
print(largestSubgrid(grid1, 4))

grid2 = [[1,1,1],[2,2,2],[3,3,3]]
print(grid2)
print(largestSubgrid(grid2, 3))
