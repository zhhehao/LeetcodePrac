#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n-1
        while True:
            while i < n and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if i > j:
                break
            elif s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
# @lc code=end

