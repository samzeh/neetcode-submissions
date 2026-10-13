# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRootVal = subRoot.val

        def sameTree(a, b):
            if not a and not b:
                return True
            
            if not a or not b:
                return False

            if a.val != b.val:
                return False
            
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        def search(node):
            if not node:
                return False

            if sameTree(node, subRoot):
                return True

            return search(node.left) or search(node.right)
        
        return search(root)
            
            

        