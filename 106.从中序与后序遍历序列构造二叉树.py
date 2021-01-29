#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode()
        root.val = postorder[-1]
        i = len(inorder)-1
        while i >= 0 and inorder[i] != root.val:
            i -= 1
            continue

        root.left = self.buildTree(inorder[0:i], postorder[0:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])

        return root
# @lc code=end

