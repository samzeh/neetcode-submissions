# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_diam = 0

        def height(node):
            if not node:
                return 0

            # calculate the height for the left and right side
            left_height = height(node.left)
            right_height = height(node.right)

            # update the max diameter
            self.max_diam = max(self.max_diam, left_height + right_height)

            #update the max height at that specific node
            return max(left_height, right_height) + 1
        
        height(root)

        return self.max_diam