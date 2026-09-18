class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            j = d.get(difference)
            if j != None:
                return [j, i]
            d[nums[i]] = i
            