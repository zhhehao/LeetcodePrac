#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # data = [
        #     (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        #     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        #     (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        #     (3, 'III'), (2, 'II'), (1, 'I')
        # ]

        data = {
            'M':1000, 'CM':900, 'D':500, 'CD':400,
            'C':100, 'XC':90, 'L':50, 'XL':40,
            'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1
        }

        ans = 0
        size = len(s)
        i = 0

        while i < size:
            if i < size - 1:
                temp = s[i] + s[i+1]
                step = 2
            else:
                temp = s[i]
                step = 1
            if temp in data:
                ans += data[temp]
                i += step
            else:
                ans += data[s[i]]
                i += 1

        return ans

# @lc code=end

