#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s:
            return ""
        n = len(t)
        d = {}
        for i in range(n):
            if t[i] not in d.keys():
                d[t[i]] = 1
            else:
                d[t[i]] += 1

        l, cnt = 0, 0
        ans = ""
        temp_ans = ""
        size = len(s)
        for r in range(size):
            temp_ans += s[r]
            if s[r] in d.keys():
                d[s[r]] -= 1
                if d[s[r]] >= 0:
                    cnt += 1
                if cnt == n:
                    while True:
                        if s[l] not in d.keys():
                            l += 1
                        elif d[s[l]] < 0:
                            d[s[l]] += 1
                            l += 1
                        else:
                            break
                    if ans == "":
                        ans = s[l:r+1]
                    elif len(s[l:r+1]) < len(ans):
                        ans = s[l:r+1]
        return ans

# @lc code=end

