#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        # print('n = ', n)
        if n == 1:
            return TreeNode(head.val)
        elif n == 2:
            p = head.next
            root = TreeNode(p.val)
            root.left = TreeNode(head.val)
            return root
        elif n == 3:
            p1 = head.next
            p2 = p1.next
            root = TreeNode(p1.val)
            root.left = TreeNode(head.val)
            root.right = TreeNode(p2.val)
            return root 
        else:
            center = n // 2
            # print('center is ', center)
            cnt = 0
            p = head
            while p:
                cnt += 1
                if cnt == center:
                    root = TreeNode(p.next.val)
                    root.right = self.sortedListToBST(p.next.next)
                    p.next = None
                    root.left = self.sortedListToBST(head)
                    return root
                p = p.next

# @lc code=end

