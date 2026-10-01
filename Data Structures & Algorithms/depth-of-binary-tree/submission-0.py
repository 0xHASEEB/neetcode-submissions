# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self._maxDepth(root.left)
        right_depth = self._maxDepth(root.right)
        if left_depth > right_depth:
            return 1+left_depth
        return 1+right_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._maxDepth(root)