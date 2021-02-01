#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(nums[0])
        elif n == 2:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
        elif n == 3:
            root = TreeNode(nums[1])
            root.left = TreeNode(nums[0])
            root.right = TreeNode(nums[2])
        else:
            root_i = n // 2
            root = TreeNode(nums[root_i])
            root.left = self.sortedArrayToBST(list(nums[0:root_i]))
            root.right = self.sortedArrayToBST(list(nums[root_i+1:]))

        return root
# @lc code=end

