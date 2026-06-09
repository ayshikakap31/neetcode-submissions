class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1 = {}
        for index,ele in enumerate(nums):
            if target-ele in dict_1:
                return [dict_1[target-ele], index]
            else:
                dict_1[ele] = index
        return None
        