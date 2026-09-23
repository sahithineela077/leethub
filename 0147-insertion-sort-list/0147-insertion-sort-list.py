# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        dummy = ListNode(0)
        temp = head

        while temp:
            next_temp = temp.next

            prev = dummy

            while prev.next and prev.next.val < temp.val:
                prev = prev.next

            temp.next = prev.next
            prev.next = temp

            temp = next_temp

        return dummy.next

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        