# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # divide and conquer with mergeTwoList
        # O(nlogk), k is number of list
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            curr = dummy = ListNode()
            # ascrending order
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None

        n, interval = len(lists), 1
        # divide
        while interval <= n:
            for start in range(0, n, interval * 2):
                if start + interval < n:
                    lists[start] = mergeTwoLists(
                        lists[start], lists[start + interval])
            interval *= 2
        return lists[0]

# Example : n = 3
# pass 1 : interval=1 <= 3, start = 0, interval = 1, 0 + 1 < 3, merge list 1 and list 2
# pass 2 : start = 2, interval = 1, 2 + 1 != 3 and 2+1=n, interval *= 2, exit from for loop
# pass 3 : interval=2 <= 3, start = 0, interval =2, 0 + 2 < 3, merge list 2 and list 3
