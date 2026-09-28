class Solution:
    def reverseBits(self, n: int) -> int:
        new_n = 0
        current = 31
        while n > 0:
            if n % 2 == 1:
                new_n |= 1 << current
            current -= 1
            n = n // 2
        return new_n