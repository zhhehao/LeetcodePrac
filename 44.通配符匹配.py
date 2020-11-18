#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 动态规划
        m, n = len(s), len(p)

        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            if p[i-1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] | dp[i-1][j]
                elif p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[m][n]


        # 超时算法
        # if not s and not p:
        #     return True

        # if not s:
        #     for i in range(len(p)):
        #         if p[i] != '*':
        #             return False
        #     return True

        # def all_star(p):
        #     if not p:
        #         return False
        #     for i in range(len(p)):
        #         if p[i] != '*':
        #             return False
        #     return True

        # if not p and s:
        #     return True if all_star(p) else False

        
        
        # def neat_start(p):
        #     rec = ''
        #     i = 0
        #     size = len(p)
        #     while i < size:
        #         rec += p[i]
        #         if p[i] != '*':
        #             i += 1
        #         else:
        #             while i < size and p[i] == '*':
        #                 i += 1

        # neat_start(p)

        # i = len(s) - 1
        # j = len(p) - 1

        # if p[j] == '*':
        #     for k in range(len(s)+1):
        #         if self.isMatch(s[:len(s)-k], p[:-1]):
        #             return True
        # elif p[j] == '?':
        #     if self.isMatch(s[:-1], p[:-1]):
        #         return True
        # else:
        #     if p[j] != s[i]:
        #         return False
        #     else:
        #         if self.isMatch(s[:-1], p[:-1]):
        #             return True

        # return False


# @lc code=end

