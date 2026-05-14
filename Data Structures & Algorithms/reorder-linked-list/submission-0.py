# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next

        slow.next = None

        second_curr = second
        second_prev = None

        while second_curr:
            next_node = second_curr.next
            second_curr.next = second_prev
            second_prev = second_curr
            second_curr = next_node
        
        second = second_prev
        first = head

        dummy = ListNode(first)
        curr = dummy
        
        
        while first and second:
            curr.next = first
            first = first.next
            curr = curr.next

            curr.next = second
            second = second.next
            curr = curr.next


        curr.next = first or second
        
        return
        