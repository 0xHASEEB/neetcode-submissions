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

    def countBits(self, n: int) -> List[int]:
        return [self.hammingWeight(num) for num in range(n+1)]