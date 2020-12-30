#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        # intervals.sort()
        # n = len(intervals)
        # ans = [intervals[0]]
        # p = 0
        # for i in range(1, n):
        #     if ans[p][1] >= intervals[i][0]:
        #         ans[p][1] = max(ans[p][1], intervals[i][1])
        #     else:
        #         ans.append(intervals[i])
        #         p += 1
        
        # return ans

        n = len(intervals)
        if n == 0:
            return [newInterval]

        for i in range(n-1, -1, -1):
            if intervals[i][0] > newInterval[1]:
                continue
            if intervals[i][1] >= newInterval[0]:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                del(intervals[i])
        
        n = len(intervals)
        if n == 0:
            return [newInterval]
        for i in range(n):
            if intervals[i][0] > newInterval[1]:
                intervals.insert(i, newInterval)
                break
        if n == len(intervals):
            intervals.append(newInterval)

        return intervals

# @lc code=end

