# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        if not q and p or not p and q:
            return False
        if q.left and not p.left or p.left and not q.left or p.right and not q.right or q.right and not p.right:
            return False
        return p.val == q.val and self._isSameTree(p.left, q.left) and self._isSameTree(p.right, q.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self._isSameTree(p, q)