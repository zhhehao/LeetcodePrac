#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        i, j = dummy, head
        while j != None:
            while j != None and j.next != None and j.next.val == j.val:
                j = j.next
            i.next = j
            i = j
            if j != None:
                j = j.next
            

        return dummy.next
# @lc code=end

