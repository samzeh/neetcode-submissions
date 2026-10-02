class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)

        leftWall = 0
        rightWall = 0

        leftHeight = [0] * l
        rightHeight = [0] * l

        water = 0

        for i in range(l):
            j = -i-1

            leftHeight[i] = leftWall
            rightHeight[j] = rightWall
            leftWall = max(leftWall, height[i])
            rightWall = max(rightWall, height[j])
        
        for i in range(l):
            water += (max(0, min(leftHeight[i], rightHeight[i]) - height[i]))
        
        return water

# The secret to this question is that the water amount is the minimum of the max left wall vs max right wall. You also need to subtract that by the current height to deal with when you are looking at the places with just a wall. You take the max of that and 0 because no negative numbers


        


        