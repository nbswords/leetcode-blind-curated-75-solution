# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # # Sol_1 : Recursion with DFS, O(N) / O(log(N)) in best case and O(N) in worst case
        # # p and q are None
        # if not p and not q:
        #     return True
        # # p or q is None
        # if not q or not p:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

        # Sol_2 : Iteration with stack, O(N) /  O(log(N)) in best case and O(N) in worst case
        stack = [(p, q)]
        while stack:
            # p 跟 q 各拿一個
            (p, q) = stack.pop()
            # 若 p 和 q 存在且相等
            if p and q and p.val == q.val:
                # 比較左和右是否相等
                stack.extend([
                    (p.left,  q.left),
                    (p.right, q.right)])
            # p 或 q 只存在一個
            elif p or q:
                return False
        return True
