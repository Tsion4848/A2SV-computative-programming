# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            moving = cur.next
            while moving and moving.val == cur.val:
                moving = moving.next
            cur.next = moving
            cur = moving
        return head

    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        if head.next:
            if head.val == head.next.val:
                head = self.deleteDuplicates(head.next)
            else:
                head.next = self.deleteDuplicates(head.next)
        return head