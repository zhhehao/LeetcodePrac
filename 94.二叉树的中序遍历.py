#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归
        # ans = []
        # def traTree(root):
        #     if not root:
        #         return
        #     traTree(root.left)
        #     ans.append(root.val)
        #     traTree(root.right)

        # traTree(root)
        # return ans

        # 迭代

        stack, ans = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                ans.append(i)
        return ans
        
# @lc code=end

