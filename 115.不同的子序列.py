#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # 递归超时
        # def solve(s, t):
        #     if len(t) == 0:
        #         return 1
        #     elif len(s) < len(t):
        #         return 0
        #     elif len(s) == len(t):
        #         for i in range(len(s)):
        #             if s[i] != t[i]:
        #                 return 0
        #         return 1
        #     else:
        #         i = 0
        #         while i < len(s) and s[i] != t[0]:
        #             i += 1
        #         if i == len(s):
        #             return 0
        #         return solve(s[i+1:], t[1:]) + solve(s[i+1:], t)          
     

        # return solve(s, t)

        # 动态规划
            n1 = len(s)
            n2 = len(t)
            dp = [[0] * (n1+1) for _ in range(n2+1)]
            for j in range(n1+1):
                dp[0][j] = 1
            for i in range(1, n2+1):
                for j in range(1, n1+1):
                    if t[i-1] == s[j-1]:
                        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                    else:
                        dp[i][j] = dp[i][j-1]
            return dp[-1][-1]

        


# @lc code=end

