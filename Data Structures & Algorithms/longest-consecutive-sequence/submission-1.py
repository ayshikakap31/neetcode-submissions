class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        n = set(nums)
        for num in nums:
            count = 1
            current = num
            if current - 1 not in n:
                while current+1 in nums:
                    current += 1
                    count += 1
                max_count = max(max_count, count)
        return max_count
        