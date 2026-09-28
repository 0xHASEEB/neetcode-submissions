class Solution:
    def hammingWeight(self, n: int) -> int:
        if n <= 1:
            return n
        count = 0
        while n >= 1:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count
        
