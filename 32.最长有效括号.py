#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 动态规划
        # ans = 0
        # size = len(s)
        # dp = [0] * size

        # for i in range(1, size):
        #     if s[i] == ')':
        #         if s[i-1] == '(':
        #             dp[i] = (dp[i-2] if i >= 2 else 0) + 2
        #         elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
        #             dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]>2 else 0) + 2
        #         ans = max(ans, dp[i])

        # return ans
        
        # 栈
        # ans = 0
        # size = len(s)
        # stack = list()
        # stack.append(-1)
        # for i in range(size):
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if not stack:
        #             stack.append(i)
        #         else:
        #             ans = max(ans, i - stack[-1])

        # return ans

        # 双向遍历
        left, right, ans = 0, 0, 0
        size = len(s)
        for i in range(size):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, 2 * right)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0
        for i in range(size-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                ans = max(ans, 2 * left)
            elif left > right:
                left, right = 0, 0

        return ans


# @lc code=end

