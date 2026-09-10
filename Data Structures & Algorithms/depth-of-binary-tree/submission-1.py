# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node, curr):
            nonlocal longest
            if not node.left and not node.right:
                longest = max(longest, curr)
            else:
                if node.left:
                    dfs(node.left, curr + 1)
                if node.right:
                    dfs(node.right, curr + 1)
        if root:
           dfs(root, 1)

        return longest