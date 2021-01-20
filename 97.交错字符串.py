#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, t = len(s1), len(s2), len(s3)
        if n + m != t:
            return False

        f = [False] * (m+1)
        f[0] = True

        for i in range(n+1):
            for j in range(m+1):
                p = i + j - 1
                if i > 0:
                    f[j] = f[j] and s1[i-1] == s3[p]
                if j > 0:
                    f[j] = f[j] or (f[j-1] and s2[j-1] == s3[p])

        return f[m]

# @lc code=end

