# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(bound: int) -> TreeNode:
            # Inorder 用來分左右和 bound
            if not inorder or inorder[-1] == bound:
                return None
            # preorder 用來找 Root
            root = TreeNode(preorder.pop())
            root.left = build(root.val)
            inorder.pop()
            root.right = build(bound)
            return root

        preorder.reverse()
        inorder.reverse()
        return build(None)
