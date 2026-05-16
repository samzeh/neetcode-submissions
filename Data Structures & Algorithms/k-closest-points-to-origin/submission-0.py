class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            distance = (i[0]**2 + i[1]**2) * -1
            heapq.heappush(heap, (distance, [i[0], i[1]]))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        
        for i in heap:
            result.append(i[1])

        return result

        



        