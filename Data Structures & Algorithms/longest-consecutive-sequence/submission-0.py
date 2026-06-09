class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        for num in nums:
            count = 1
            while num+1 in nums:
                num += 1
                count += 1
            max_count = max(max_count, count)
        return max_count
        