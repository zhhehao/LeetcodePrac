#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # i = 0
        # while True:
        #     i2 = i ** 2
        #     if i2 == x:
        #         return i
        #     elif i2 > x:
        #         return i - 1
        #     else:
        #         i += 1

        # 方法一：袖珍计算器算法
        # import math
        # if x == 0:
        #     return 0
        # ans = int(math.exp(0.5 * math.log(x)))
        # return ans + 1 if (ans + 1) ** 2 <= x else ans

        # 方法二：二分查找
        # l, r, ans = 0, x, -1
        # while l <= r:
        #     mid = (l+r) // 2
        #     if mid * mid <= x:
        #         ans = mid
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return ans

        # 方法三：牛顿迭代
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi
        return int(x0)
# @lc code=end

