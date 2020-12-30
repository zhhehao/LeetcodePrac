#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        ans = []
        candidates.sort()
        def solve(rec, index, new_target):
            if new_target == 0:
                ans.append(rec[:])
                return
            for i in range(index, size):
                if candidates[i] > new_target:
                    break
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                rec.append(candidates[i])
                solve(rec, i+1, new_target-candidates[i])
                rec.pop()
            
        solve([], 0, target)
        return ans
# @lc code=end

