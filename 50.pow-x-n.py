#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 快速幂 + 递归
        # def quickMul(N):
        #     if N == 0:
        #         return 1.0
        #     y = quickMul(N // 2)
        #     return y * y if N % 2 == 0 else y * y * x

        # return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

        #  快速幂 + 迭代
        def quickMul(N):
            ans = 1.0
            x_contribute = x
            while N > 0:
                if N % 2 == 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                N //= 2
            return ans
            
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)
# @lc code=end

