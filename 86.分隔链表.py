#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        i = dummy
        while i != None and i.next != None and i.next.val < x:
            i = i.next

        if i == None:
            return dummy.next

        j = i
        while j != None and j.next != None:
            if j.next.val < x:
                move_node = j.next
                j.next = j.next.next
                move_node.next = i.next
                i.next = move_node
                i = i.next
            else:
                j = j.next


        return dummy.next
    # @lc code=end

