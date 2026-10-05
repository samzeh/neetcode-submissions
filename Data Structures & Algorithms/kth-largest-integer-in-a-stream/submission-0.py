class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i in range(len(nums)):
            heapq.heappush(self.heap, nums[i])
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            for i in range(self.k-1):
                heapq.heappop(self.heap)

        return(heapq.heappop(self.heap))


        
        
