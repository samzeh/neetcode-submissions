# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.result = True

        def check(node1, node2):
            if not node1 or not node2:
                self.result = False
                return

            if (node1.left and node2.left):
                self.result = node1.left.val == node2.left.val
                return
            
            if node1.right and node2.right:
                self.result = node1.right.val == node2.right.val
                return

            check(node1.left, node2.left)
            check(node1.right, node2.right)
        
        check(p, q)
        return self.result
        


        