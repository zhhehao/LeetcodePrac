#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder(root, nums):
            if not root:
                 return
            inorder(root.left, nums)
            nums.append(root.val)
            inorder(root.right, nums)

        def findTwoSwapped(nums):
            n = len(nums)
            x, y = -1, -1
            for i in range(n-1):
                if nums[i+1] < nums[i]:
                    y = nums[i+1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover(root, count, x, y):
            if root:
                if root.val == x or root.val == y:
                    root.val = y if root.val == x else x
                    count -= 1
                    if count == 0:
                        return
                recover(root.right, count, x, y)
                recover(root.left, count, x, y)

        nums = []
        inorder(root, nums)
        x, y = findTwoSwapped(nums)
        recover(root, 2, x, y)


# @lc code=end

