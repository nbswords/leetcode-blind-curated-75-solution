# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # map(function, iterable, ...)
        # EX: map(square, [1,2,3,4,5]) => [1, 4, 9, 16, 25]
        # Recurive find maxDepth of left and right plus current level
        return max(map(self.maxDepth, (root.left, root.right))) + 1 if root else 0
