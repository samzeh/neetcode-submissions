class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)

        left = 0
        right = 0
        maxFruits = 0

        while right < len(fruits):
            count[fruits[right]] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            
            maxFruits = max(maxFruits, right-left+1)
            right += 1
            
        return maxFruits
        