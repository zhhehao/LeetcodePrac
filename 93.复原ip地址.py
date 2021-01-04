#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        def solve(i, rec, step):
            if i == n:
                if step == 4:
                    # print(rec)
                    ans.append(rec[:-1])
                return
            if step == 4 and i != n:
                return
            if s[i] == '0':
                rec1 = rec + '0.'
                solve(i+1, rec1, step+1)
            elif 3 <= int(s[i]):
                rec1 = rec + s[i] + '.'
                solve(i+1, rec1, step+1)
                if i + 1 < n:
                    rec2 = rec + s[i] + s[i+1] + '.'
                    solve(i + 2, rec2, step+1)
            elif s[i] == '1':
                rec1 = rec + s[i] + '.'
                solve(i+1, rec1, step+1)
                if i + 1 < n:
                    rec2 = rec + s[i] + s[i+1] + '.'
                    solve(i + 2, rec2, step+1)
                if i + 2 < n:
                    rec3 = rec + s[i] + s[i+1] + s[i+2] + '.'
                    solve(i + 3, rec3, step+1)
            elif s[i] == '2':
                rec1 = rec + s[i] + '.'
                solve(i+1, rec1, step+1)
                if i + 1 < n:
                    rec2 = rec + s[i] + s[i+1] + '.'
                    solve(i + 2, rec2, step+1)
                if i + 2 < n:
                    if int(s[i+1]) < 5 or (s[i+1] == '5' and int(s[i+2]) <= 5):
                        rec3 = rec + s[i] + s[i+1] + s[i+2] + '.'
                        solve(i + 3, rec3, step+1)

        solve(0, '', 0)
        return ans
# @lc code=end

