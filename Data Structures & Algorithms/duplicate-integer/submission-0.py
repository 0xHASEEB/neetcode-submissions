class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if d.get(n) != None:
                return True
            d[n] = 0
        return False 