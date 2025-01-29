# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def traverse(node: TreeNode, level: int) -> None:
            if not node:
                return None
            # a level traversal finished
            if len(result) == level:
                result.append([])
            result[level].append(node.val)

            # Inorder Recursion traversal
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        result = []
        traverse(root, level=0)
        return result
