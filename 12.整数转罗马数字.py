#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        # 贪心
        # data = [
        #     (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        #     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        #     (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        #     (3, 'III'), (2, 'II'), (1, 'I')
        # ]

        # ans = ''
        # for n, s in data:
        #     while num >= n:
        #         ans += s
        #         num -= n
        #     if num == 0:
        #         break
        # return ans

        # 打表
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]

# @lc code=end

