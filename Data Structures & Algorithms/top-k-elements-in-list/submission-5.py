import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Frequency map
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Min heap of size k
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract the numbers
        return [num for count, num in heap]