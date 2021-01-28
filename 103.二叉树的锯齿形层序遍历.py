#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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

        for i in range(1, len(rec), 2):
            rec[i].reverse()
        
        return rec
# @lc code=end

