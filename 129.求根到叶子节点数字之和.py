#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    rec = 0
    def sumNumbers(self, root: TreeNode) -> int:

        def solve(num, root):
            num = num * 10 + root.val
            if not root.left and not root.right:
                self.rec += num
                return

            if root.left:
                solve(num, root.left)
            
            if root.right:
                solve(num, root.right)

        solve(0, root)
        return self.rec


# @lc code=end

