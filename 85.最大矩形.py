#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # DP
        # max_area = 0
        # dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == '0':
        #             continue
        #         width = dp[i][j] = dp[i][j-1] + 1 if j else 1
        #         for k in range(i, -1, -1):
        #             width = min(width, dp[k][j])
        #             max_area = max(max_area, width * (i-k+1))

        # 栈 84题
        if not matrix:
            return 0

        maxarea = 0

        def leetcode84(heights):
            stack = [-1]
            maxarea = 0
            for i in range(len(heights)):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    maxarea = max(maxarea, heights[stack.pop()]*(i - stack[-1] -1))
                stack.append(i)

            while stack[-1] != -1:
                maxarea = max(maxarea, heights[stack.pop()] * (len(heights) - stack[-1] -1))
            return maxarea


        
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            maxarea= max(maxarea, leetcode84(dp))
        return maxarea
# @lc code=end

