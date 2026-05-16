class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stone_heap = []
        for i in stones:
            stone_heap.append(i*-1)
        
        heapq.heapify(stone_heap)

        while len(stone_heap) > 1:
            stone_1 = heapq.heappop(stone_heap)
            stone_2 = heapq.heappop(stone_heap)

            if stone_1 != stone_2:
                result = stone_1 - stone_2
                heapq.heappush(stone_heap, result)

        if len(stone_heap) > 0:
            return stone_heap[0] * -1
        
        return 0
            



        