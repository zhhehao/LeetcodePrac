#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        rec = [[1],[1,1]]
        n = rowIndex - 1
        while n > 0:
            ans = []
            m = len(rec[-1]) - 1
            for i in range(m):
                ans.append(rec[-1][i] + rec[-1][i+1])
            rec.append([1] + ans + [1])
            n -= 1
        return rec[-1]
# @lc code=end

