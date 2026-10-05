class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for i in nums:
            mySet.add(i)
        return list(mySet)
