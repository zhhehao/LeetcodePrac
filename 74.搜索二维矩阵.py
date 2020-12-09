# @before-stub-for-debug-begin
from python3problem74 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2 
            i = mid // n 
            j = mid % n 
            # print(mid, i, j, matrix[i][j])
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

        
# @lc code=end

