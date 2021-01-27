#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 迭代
        # s1, s2 = [root], [root]
        # while len(s1) > 0:
        #     n1 = s1.pop()
        #     n2 = s2.pop()
        #     if not n1 and not n2:
        #         continue
        #     if (not n1 and n2) or (n1 and not n2):
        #         return False
        #     if n1.val != n2.val:
        #         return False
        #     s1.extend([n1.left, n1.right])
        #     s2.extend([n2.right, n2.left])

        # return True       

        # 递归
        def solve(r1, r2):
            if not r1 and not r2:
                return True
            if (not r1 and r2) or (r1 and not r2):
                return False
            if r1.val != r2.val:
                return False
            if not solve(r1.left, r2.right):
                return False
            if not solve(r1.right, r2.left):
                return False
            return True

        return solve(root, root)
# @lc code=end

