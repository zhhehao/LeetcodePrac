#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        tail = head
        p = head.next
        head.next = None
        count = 1
        while count < k and p:
            temp = p.next
            p.next = dummy.next
            dummy.next = p
            p = temp
            count += 1

        if count == k:
            tail.next = self.reverseKGroup(p, k)
            return dummy.next
        else:
            dummy2 = ListNode()
            p = dummy.next
            while p:
                temp = p.next
                p.next = dummy2.next
                dummy2.next = p
                p = temp
            return dummy2.next



        
# @lc code=end

