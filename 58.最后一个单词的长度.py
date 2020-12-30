# @before-stub-for-debug-begin
from python3problem58 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        r = n - 1
        while r >= 0 and not s[r].isalpha():
            r -= 1
        l = r
        while l >= 0 and s[l].isalpha():
            l -= 1
        # print(p)
        if l < 0:
            return r+1
        else:
            return r-l
# @lc code=end

