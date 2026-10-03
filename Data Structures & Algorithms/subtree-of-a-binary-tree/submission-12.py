# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, foo, bar):
        if not foo and not bar:
            return True
        if not foo or not bar or foo.val != bar.val:
            return False
        else:
            return self.isSameTree(foo.left, bar.left) and self.isSameTree(foo.right, bar.right)