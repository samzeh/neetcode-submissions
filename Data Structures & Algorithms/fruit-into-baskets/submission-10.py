class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = []
        left = 0
        right = 0
        maxFruit = 0

        while right < len(fruits):            
            # fruit is already in basket -> we increment right + recalculate maxFruit
            if fruits[right] in basket:
                right += 1

            # fruit is not in basket -> check length basket and then append the fruit on if valid
            elif len(basket) < 2:
                basket.append(fruits[right])
                right += 1
            else:
                last = fruits[right - 1]
                # evict the type that isn't the most recent fruit
                basket.remove(basket[0] if basket[0] != last else basket[1])
                # move left to the start of the final run of `last`
                left = right - 1
                while fruits[left - 1] == last:
                    left -= 1
                basket.append(fruits[right])
                right += 1
            maxFruit = max(right-left, maxFruit)
        
        return maxFruit