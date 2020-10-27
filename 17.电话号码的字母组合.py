#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {
            '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', 
            '7':'pqrs', '8':'tuv', '9':'wxyz'
        }
        size = len(digits)
        ans = []
        s = ''

        def solve(s, p):
            if p == size:
                ans.append(s)
                return
            alpha = d[digits[p]]
            for i in range(len(alpha)):
                s += alpha[i]
                solve(s, p+1)
                s = s[:-1]
        
        solve(s, 0)
        return ans
                    

# @lc code=end

