#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归
        # def getVals(root):
        #     min_val, max_val = root.val, root.val
        #     if root.left:
        #         min_left, max_left, status_left = getVals(root.left)
        #         if status_left == False or min_left >= root.val or max_left >= root.val:
        #             return (None, None, False)
        #         else:
        #             min_val = min(min_val, min_left)
        #             max_val = max(max_val, max_left)
        #     if root.right:
        #         min_right, max_right, status_right = getVals(root.right)
        #         if status_right == False or min_right <= root.val or min_right <= root.val:
        #             return (None, None, False)
        #         else:
        #             min_val = min(min_val, min_right)
        #             max_val = max(max_val, max_right)

        #     return (min_val, max_val, True)

        # return getVals(root)[2]

        # 中序遍历
        
        stack = []
        stack.append(root)
        fVal = float('-inf')

        while len(stack) > 0:
            # print("There is ", len(stack), " items before pop().")
            node = stack.pop()
            # print("There is ", len(stack), " items after pop().")
            if isinstance(node, int):
                if node <= fVal:
                    return False
                else:
                    fVal = node
            else:
                if node.right:
                    stack.append(node.right)
                stack.append(node.val)
                if node.left:
                    stack.append(node.left)
                

        return True




# @lc code=end

