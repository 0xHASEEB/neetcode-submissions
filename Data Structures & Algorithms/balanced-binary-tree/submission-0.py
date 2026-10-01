# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _isBalanced(self, root: Optional[TreeNode]) -> List[int, bool]:
        if not root:
            return [0, True]
        left = self._isBalanced(root.left)
        right = self._isBalanced(root.right)
        if left[1] == False or right[1] == False:
            return [0, False]
        if abs(left[0]-right[0]) > 1:
            return [0, False]
        if left[0] > right[0]:
            return [left[0]+1, True]
        return [right[0]+1, True]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._isBalanced(root)[1]