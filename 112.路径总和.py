#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return True if root.val == targetSum else False
        if root.left:
            if self.hasPathSum(root.left, targetSum-root.val):
                return True
        if root.right:
            if self.hasPathSum(root.right, targetSum-root.val):
                return True
        return False
# @lc code=end

