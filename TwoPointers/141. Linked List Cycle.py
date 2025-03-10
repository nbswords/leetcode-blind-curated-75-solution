# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        walker, runner = head, head # Two pointers
        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker is runner: return True
        return False        