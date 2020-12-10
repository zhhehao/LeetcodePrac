#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def solve(rec, step, start):
            if step == k:
                ans.append(list(rec))
                return
            
            for i in range(start, n+1):
                rec.append(i)
                solve(rec, step+1, i+1)
                rec.pop()
            return 


        solve([], 0, 1)
        return ans

# @lc code=end

