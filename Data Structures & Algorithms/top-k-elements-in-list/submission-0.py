import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<2:
            return nums
        dict_1 = {}
        out = []
        for ele in nums:
            if ele not in dict_1:
                dict_1[ele] = 1
            else:
                dict_1[ele] += 1
        heap_items = [(-vals,keys) for keys,vals in dict_1.items()]
        heapq.heapify(heap_items)

        for index in range(k):
            out.append(heapq.heappop(heap_items)[1])
        return out
            
        