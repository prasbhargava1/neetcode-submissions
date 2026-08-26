from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        heap = []
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        
        for num, count in freq.items():
            heapq.heappush(heap,(-count,num))
        result = []

        for _ in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)

    
        return result

        