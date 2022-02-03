
stones = [10, 30, 40, 20] # initialize input here
cost = [-1 for i in stones]
cost[0] = 0
cost[1] = abs(stones[1] - stones[0])

def calcCost(N):
    if cost[N - 1] != -1:
        return cost[N-1]
    mCost = min(calcCost(N - 2) + abs(stones[N - 2] - stones[N-3]), calcCost(N - 1) + abs(stones[N - 1] - stones[N -2]))
    cost[N - 1] = mCost
    return mCost

print(calcCost(4))