class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) < 2:
            return [0]
        output = [1]*len(nums)
        # For prefix
        prefix_prod = 1
        for index in range(len(nums)):
            output[index] = prefix_prod
            prefix_prod *= nums[index]
        # For suffix
        suffix_prod = 1
        for index in range(len(nums)-1,-1,-1):
            output[index] *= suffix_prod
            suffix_prod *= nums[index] 
        return output
        