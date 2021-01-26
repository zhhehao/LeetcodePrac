#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        s1, s2 = [], []
        s1.append(p)
        s2.append(q)
        while len(s1) > 0:
            n1 = s1.pop()
            n2 = s2.pop()
            if not n1 and not n2:
                continue
            if (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
                return False
            s1.append(n1.left)
            s2.append(n2.left)
            s1.append(n1.right)
            s2.append(n2.right)

        return True
            



# @lc code=end

