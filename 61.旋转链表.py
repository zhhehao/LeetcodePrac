#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        length = 0
        p = head
        tail = head
        while p != None:
            length += 1
            if p.next == None:
                tail = p
            p = p.next

        k = k % length

        if k == 0:
            return head

        cnt = length - k - 1

        p = head
        while cnt > 0:
            p = p.next
            cnt -= 1

        dummy = ListNode()
        dummy.next = p.next
        p.next = None
        tail.next = head

        return dummy.next

        

# @lc code=end

