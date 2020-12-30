# @before-stub-for-debug-begin
from python3problem39 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        ans = []
        def solve(rec, index, new_target):
            if new_target == 0:
                # print("rec is", rec)
                ans.append(list(rec))
                # print("ans is", ans)
                return
            for i in range(index, size):
                if candidates[i] <= new_target:
                    rec.append(candidates[i])
                    solve(rec, i, new_target-candidates[i])
                    rec.pop()
            
        solve([], 0, target)
        return ans

    
# @lc code=end

