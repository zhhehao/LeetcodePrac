#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        up = 1
        while i >= 0:
            value = digits[i] + up
            digits[i] = value % 10
            up = value // 10
            if up == 0:
                break
            else:
                i -= 1

        return [up] + digits if up != 0 else digits


        

# @lc code=end

