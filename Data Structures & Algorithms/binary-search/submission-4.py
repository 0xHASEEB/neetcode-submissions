class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, f, b = 0, 0, len(nums)
        while f != b:
            i = (b+f) // 2
            if target == nums[i]:
                return i
            elif target > nums[i]:
                f = i+1
            else:
                b = i
        return -1