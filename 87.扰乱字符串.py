#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)
        if n1 != n2:
            return False

        if s1 == s2:
            return True
        
        letters = [0] * 26
        for i in range(n1):
            letters[ord(s1[i])-ord('a')] += 1
            letters[ord(s2[i])-ord('a')] -= 1
        
        for i in range(26):
            if letters[i] != 0:
                return False

        for i in range(1, n1):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[i:], s2[0:n2-i]) and self.isScramble(s1[0:i], s2[n2-i:]):
                return True
        
        return False

        

        

# @lc code=end

