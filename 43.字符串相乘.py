# @before-stub-for-debug-begin
from python3problem43 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == '0' or num2[0] == '0':
            return '0'

        n1 = len(num1)
        n2 = len(num2)

        if n1 < n2:
            num1, num2 = num2, num1
            n1, n2 = n2, n1
                    
        ans = 0
        ten = 1
        up = 0
        for j in range(n2-1, -1, -1):
            temp_ans = 0
            up = 0
            inner_ten = 1
            for i in range(n1-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                mul += up
                temp_ans = temp_ans + (mul % 10) * inner_ten
                up = mul // 10
                inner_ten *= 10
            if up != 0:
                temp_ans = temp_ans +  up * inner_ten
            # print("temp_ans is ", temp_ans)
            ans = ans  + temp_ans * ten
            ten *= 10
        # print(up)
        # if up != 0:
        #     ans = ans + up * ten
        return str(ans)

# @lc code=end

