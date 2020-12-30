# @before-stub-for-debug-begin
from python3problem56 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        if n <= 1:
            return intervals
        ans = [intervals[0]]
        p = 0
        for i in range(1, n):
            if ans[p][1] >= intervals[i][0]:
                ans[p][1] = max(intervals[i][1], ans[p][1])
            else:
                ans.append(intervals[i])
                p += 1

        return ans




# @lc code=end

