#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode()
        root.val = preorder[0]
        i = 0
        while i < len(inorder) and inorder[i] != root.val:
            i += 1
            continue

        root.left = self.buildTree(preorder[1:1+i], inorder[0:i])
        root.right = self.buildTree(preorder[1+i:], inorder[i+1:])

        return root
# @lc code=end

