class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            summ = numbers[left]+numbers[right]
            if summ == target:
                return [numbers[left], numbers[right]]
            elif summ > target:
                right -= 1
            else:
                right += 1
        
        