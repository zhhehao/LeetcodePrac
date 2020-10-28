#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n_len = len(needle)

        def is_match(s1, s2):
            for i in range(n_len):
                if s1[i] != s2[i]:
                    return False
            return True

        i = 0
        h_len = len(haystack)
        while i + n_len <= h_len:
            if haystack[i] != needle[0]:
                i += 1
                continue
            if i + n_len <= h_len:
                if is_match(needle, haystack[i:i+n_len]):
                    return i
                i += 1
        
        return -1

# @lc code=end

