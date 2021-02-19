#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        rec = [[1],[1,1]]
        n = numRows - 2
        while n > 0:
            ans = []
            m = len(rec[-1]) - 1
            for i in range(m):
                ans.append(rec[-1][i] + rec[-1][i+1])
            rec.append([1] + ans + [1])
            n -= 1
        return rec

# @lc code=end

