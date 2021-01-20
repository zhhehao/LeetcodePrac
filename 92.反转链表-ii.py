#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p, left, right = dummy, dummy, dummy
        cnt = 0
        stack = []
        while p != None:
            if m <= cnt < n:
                stack.append(p)
            elif cnt == m - 1:
                left = p
            elif cnt == n:
                stack.append(p)
                right = p.next
                while len(stack) != 0:
                    left.next = stack.pop()
                    left = left.next
                left.next = right
                return dummy.next
            p = p.next
            cnt += 1
        return dummy.next
                


# @lc code=end

