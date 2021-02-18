#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    last, nextStart = None, None
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def handle(p):
            if self.last:
                self.last.next = p
            if not self.nextStart:
                self.nextStart = p
            self.last = p

        start = root
        while start:
            self.last = None
            self.nextStart = None
            p = start
            while p:
                if p.left:
                    handle(p.left)
                if p.right:
                    handle(p.right)
                p = p.next
            start = self.nextStart
        
        return root
# @lc code=end

