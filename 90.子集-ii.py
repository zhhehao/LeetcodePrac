#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def solve(i, sub, rec):
            if i == len(nums):
                return
            rec.add(tuple(sub))
            solve(i+1, list(sub), rec)
            sub.append(nums[i])
            rec.add(tuple(sub))
            solve(i+1, list(sub), rec)

        rec = set()
        solve(0, [], rec)
        return list(rec)

# @lc code=end

