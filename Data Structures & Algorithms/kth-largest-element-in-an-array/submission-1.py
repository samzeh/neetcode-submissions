class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        new_nums = []
        for i in range(len(nums)):
            new_nums.append(nums[i]*-1)

        heapq.heapify(new_nums)

        for i in range(k-1):
            heapq.heappop(new_nums)
        
        result = heapq.heappop(new_nums)

        return result * -1        