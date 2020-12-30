#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range (0, n-1):
            for j in range(0, n-1):
                if i + j < n-1:
                    new_i = n - j - 1
                    new_j = n - i - 1
                    matrix[i][j], matrix[new_i][new_j] = matrix[new_i][new_j], matrix[i][j]
        
        for i in range(0, n // 2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

# @lc code=end

