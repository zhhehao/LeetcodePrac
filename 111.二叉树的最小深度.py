#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        min_depth = 1000000
        stack = [(root, 1)]

        while len(stack) > 0:
            # print(len(stack), min_depth)
            node, depth = stack.pop()
            if not node.left and not node.right:
                min_depth = min(depth, min_depth)
                continue
            if node.left and depth + 1 < min_depth:
                stack.append((node.left, depth+1))
            if node.right and depth + 1 < min_depth:
                stack.append((node.right, depth+1))

        return min_depth


# @lc code=end

