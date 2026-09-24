class Solution:        
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        d = {length: 0, length+1: 0}
        for i in range(length-1, -1, -1):
            with_i = nums[i] + d[i+2]
            without_i = d[i+1]
            d[i] = max(with_i, without_i)
        return d[0]