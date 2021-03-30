#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_par(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        rec = []
        def solve(s, ans):
            if not s or is_par(s) :
                ans.append(s)
                rec.append(list(ans))
                ans.pop()

            n = len(s)
            for i in range(1, n):
                if is_par(s[:i]):
                    ans.append(s[:i])
                    solve(s[i:], ans)
                    ans.pop()

        solve(s, [])

        return rec

# @lc code=end

