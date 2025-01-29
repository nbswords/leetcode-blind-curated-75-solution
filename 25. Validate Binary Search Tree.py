# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Recursion Time: O(N)/ Space: O(H)
        def is_valid(node, left=float('-inf'), right=float('inf')) -> bool:
            if not node:
                return True
            if node.val <= left or right <= node.val:
                return False
            return (is_valid(node.left, left, node.val) and
                    is_valid(node.right, node.val, right))
        return is_valid(root)

# 另解 : Inorder Morris Traversal Time :O(N) / Space : O(1)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        current = float('-inf')
        while root:
            # 若 root 不存在
            if root.val <= current:
                return False
            # 當前節點的左節點不為空
            if node := root.left:
                # 左節點的右子節點不為空且不為 root
                while node.right and node.right is not root:
                    node = node.right
                # 左節點的右子節點為 root (當前節點)
                if node.right is root:
                    # 將右節點重新設定為空來恢復樹的形狀
                    node.right = None
                    # 輸出當前節點並且把右節點作為新的當前節點
                    current = root.val
                    root = root.right
                # 左節點的右子節點為空
                else:
                    # 將右節點設定為當前節點並且把左節點作為新的當前節點
                    node.right = root
                    root = root.left
            # 當前節點的左孩子為空
            else:
                # 輸出當前節點並且把右節點作為新的當前節點
                current = root.val
                root = root.right
        return True
