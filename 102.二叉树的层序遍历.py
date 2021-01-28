#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        rec, queue = [], []
        queue.append((root, 0))
        head, tail = 0, 0
        while head <= tail:
            node, level = queue[head]
            head += 1
            rec.append([])
            rec[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
                tail += 1
            if node.right:
                queue.append((node.right, level+1))
                tail += 1
            while head <= tail and queue[head][1] == level:
                node, _ = queue[head]
                head += 1
                rec[level].append(node.val)
                if node.left:
                    queue.append((node.left, level+1))
                    tail += 1
                if node.right:
                    queue.append((node.right, level+1))
                    tail += 1
        
        return rec

# @lc code=end

