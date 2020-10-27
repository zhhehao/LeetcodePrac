#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 优先队列
        # class tempListNode:
        #     def __init__(self, x):
        #         self.node = x
        #         self.val = x.val

        #     def __lt__(self, other):
        #         return self.val < other.val

        #     def get_node(self):
        #         return self.node

        # from queue import PriorityQueue 
        # q = PriorityQueue()
        # for n in lists:
        #     if n:
        #         q.put(tempListNode(n))

        # dummy = ListNode(0)
        # p = dummy
        # while not q.empty():
        #     ln = q.get()
        #     tn = ln.get_node()
        #     p.next = tn
        #     p = p.next
        #     if tn.next:
        #         q.put(tempListNode(tn.next))

        # return dummy.next

        # 分治

        def merge(left, right):
            if left == right:
                return lists[left]
            if left > right:
                return None
            mid = (left + right) // 2
            return mergeTwoLists(merge(left, mid), merge(mid + 1, right))

        def mergeTwoLists(a, b):
            if not a or not b:
                return a if a else b
            head = ListNode(0)
            tail, aPtr, bPtr = head, a, b
            while aPtr and bPtr:
                if aPtr.val < bPtr.val:
                    tail.next, aPtr = aPtr, aPtr.next
                else:
                    tail.next, bPtr = bPtr, bPtr.next
                tail = tail.next

            tail.next = aPtr if aPtr else bPtr
            return head.next

        return merge(0, len(lists) - 1)

# @lc code=end

