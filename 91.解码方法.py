#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0] * (len(s)+1)
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i+1] = dp[i-1]
                else:
                    return 0
            elif (s[i-1] == '1') or (s[i-1] == '2' and int(s[i]) <= 6):
                dp[i+1] = dp[i] + dp[i-1]
            else:
                dp[i+1] = dp[i]

        return dp[-1]

# @lc code=end
