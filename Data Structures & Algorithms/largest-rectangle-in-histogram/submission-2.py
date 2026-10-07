class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h,j = stack.pop()
                width = i-j
                area = h*width
                maxArea = max(maxArea, area)
                start = j
            stack.append((height, start))
        
        while stack:
            h, j = stack.pop()
            w = len(heights) - j
            area = h*w
            maxArea = max(maxArea, area)

        return maxArea



        