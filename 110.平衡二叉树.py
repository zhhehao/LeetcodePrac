#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(root):
            if not root:
                return (True, 0)
            if not root.left and not root.right:
                return (True, 1)
            elif not root.left and root.right:
                r, h = getHeight(root.right)
                if not r or h > 1:
                    return (False, None)
                else:
                    return (True, 2)
            elif root.left and not root.right:
                r, h = getHeight(root.left)
                if not r or h > 1:
                    return (False, None)
                else:
                    return (True, 2)
            else:
                r1, h1 = getHeight(root.left)
                r2, h2 = getHeight(root.right)
                if not r1 or not r2 or abs(h2-h1) > 1:
                    return (False, None)
                else:
                    return (True, max(h2, h1)+1)

        r, h = getHeight(root)
        return r
                    

# @lc code=end

