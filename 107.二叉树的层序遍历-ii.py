#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        rec = []
        stack = [(root, 0)]
        while len(stack) > 0:
            node, level = stack.pop()
            while len(rec) <= level:
                rec.append([])
            rec[level].append(node.val)
            if node.right:
                stack.append((node.right, level+1))
            if node.left:
                stack.append((node.left, level+1))
        rec.reverse()
        return rec

# @lc code=end

