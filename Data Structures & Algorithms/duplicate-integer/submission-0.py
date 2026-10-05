class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set = set()
        for i in nums:
            if i in nums:
                return True
            else:
                set.add(i)
            