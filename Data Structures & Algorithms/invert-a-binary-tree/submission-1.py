# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _invert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp
        self._invert(root.left)
        self._invert(root.right)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self._invert(root)
        