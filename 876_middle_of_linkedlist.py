from typing import Optional, Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        mid = head
        end = head

        while end is not None and end.next is not None:
            mid = mid.next
            end = end.next.next
        
        return mid.val
    
sol = Solution
n1 = ListNode(1, None)
n2 = ListNode(2, n1)
n3 = ListNode(3, n2)
n4 = ListNode(4, n3)
n5 = ListNode(5, n4)
print(sol.middleNode(Self, head=n5))