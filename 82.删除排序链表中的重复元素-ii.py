#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = dict()
        i = head
        while i != None:
            if i.val in d.keys():
                d[i.val] += 1
            else:
                d[i.val] = 1
            i = i.next

        dummy = ListNode()
        i, j = dummy, head
        while j != None:
            while j != None and d[j.val] > 1:
                j = j.next
            i.next = j
            i = j
            if j != None:
                j = j.next
                
        return dummy.next
# @lc code=end

