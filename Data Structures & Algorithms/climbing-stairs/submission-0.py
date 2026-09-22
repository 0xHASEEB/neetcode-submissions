class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        d = {1: 1, 2: 2}
        for k in range(3, n):
            d[k] = d[k-1] + d[k-2]
        return d[n-1] + d[n-2] 