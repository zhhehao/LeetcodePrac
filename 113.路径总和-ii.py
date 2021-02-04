#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []
        def solve(root, target, path):
            if not root:
                return 
            if not root.left and not root.right:
                if target == root.val:
                    rec = list(path)
                    rec.append(root.val)
                    ans.append(rec)
                return
            if root.left:
                solve(root.left, target-root.val, path + [root.val])
            if root.right:
                solve(root.right, target-root.val, path + [root.val])
        
        solve(root, targetSum, [])
        return ans
# @lc code=end

