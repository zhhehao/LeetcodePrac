# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # def solve(d1, d2, count):
        #     while d1 > d2:
        #         d1 -= d2
        #         count += 1
        #     return count

        # if not dividend:
        #     return 0
        # if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
        #     sign = -1
        # else:
        #     sign = 1

        # MIN_INT = -2147483648
        # MAX_INT = 2147483647

        # if dividend == MIN_INT and divisor == MIN_INT:
        #     return 1

        # if dividend == MIN_INT and divisor != MIN_INT:
        #     if divisor == 1:
        #         return MIN_INT
        #     if divisor == -1:
        #         return MAX_INT
        #     return sign * solve(dividend - abs(divisor), abs(divisor), 1)

        # if dividend != MIN_INT and divisor == MIN_INT:
        #     return 0

        # dividend, divisor = abs(dividend), abs(divisor)

        # if dividend == divisor:
        #     return sign * 1

        # if dividend < divisor:
        #     return 0

        # if divisor == 1:
        #     return sign * dividend
     
        # return sign * solve(dividend, divisor, 0)

        MIN_INT, MAX_INT = -2147483648, 2147483647
        flag = 1
        if dividend < 0:
            flag, dividend = -flag, -dividend
        if divisor < 0:
            flag, divisor = -flag, -divisor

        def div(dividend, divisor):
            if dividend < divisor:
                return 0
            cur = divisor
            multiple = 1
            while cur + cur < dividend:
                cur += cur
                multiple += multiple
            return multiple + div(dividend - cur, divisor)

        res = div(dividend, divisor)
        res = res if flag > 0 else -res

        if res < MIN_INT:
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT
        

# @lc code=end

