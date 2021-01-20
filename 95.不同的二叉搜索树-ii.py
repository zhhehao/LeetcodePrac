#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def geTree(start, end):
            if start > end:
                return [None,]
            
            ans = []

            for i in range(start, end+1):
                rTree = geTree(i+1, end)
                lTree = geTree(start, i-1)

                for l in lTree:
                    for r in rTree:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)

            return ans

        return geTree(1, n) if n else []
        
# @lc code=end

