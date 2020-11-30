# @before-stub-for-debug-begin
from python3problem60 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(n, k, index, path):
            if index == n:
                return 
            cnt = factorial[n - 1 - index]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(n, k, index+1, path)
                return

        if n == 0:
            return ""

        used = [False for _ in range(n+1)]
        path = []
        factorial = [1 for _ in range(n+1)]
        for i in range(2, n+1):
            factorial[i] = factorial[i-1] * i

        dfs(n, k, 0, path)
        return ''.join([str(num) for num in path])
        


            

# @lc code=end

