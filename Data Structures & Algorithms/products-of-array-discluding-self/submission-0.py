class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) < 2:
            return [0]
        output = [1]*len(nums)
        # For suffix
        for index in range(len(nums)):
             left = index+1
             while left < len(nums):
                output[index] *= nums[left]
                left += 1
        # For prefix
        for index in range(len(nums)):
            right = index-1
            while right >=0:
                output[index] *= nums[right]
                right -= 1
        return output
        