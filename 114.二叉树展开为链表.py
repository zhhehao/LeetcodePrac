#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return []
        dummy = TreeNode()
        p = dummy
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            p.right = node
            p = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            p.left = None

        return dummy.right

# @lc code=end

