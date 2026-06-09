class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        else:
            unique_ele = set(nums)
            if len(unique_ele) == len(nums):
                return False
            else:
                return True