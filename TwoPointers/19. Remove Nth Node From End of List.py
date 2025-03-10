# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Find the node which need to be deleted
        runner = head
        for _ in range(n):
            runner = runner.next
        # Create a dummy node to point new Linked List
        # It can also deal with corner case
        # For example, only one node
        # dummy and walker init point to head
        dummy = walker = ListNode(next=head)

        while runner:  # Until runner node is NULL
            walker = walker.next  # walker is slow
            runner = runner.next  # runner is fast

        # After while loop
        # walker is at the previous node of n_th node
        walker.next = walker.next.next
        return dummy.next
