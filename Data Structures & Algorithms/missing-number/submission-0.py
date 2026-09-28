class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            count = count | (1 << n)
        
        missing = 0
        while count % 2 != 0: 
            missing += 1            
            count = count // 2
        return missing