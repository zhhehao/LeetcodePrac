#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        def read_it(s):
            ans = ''
            size = len(s)
            sub_str = []
            sub_str.append(s[0])
            i = 1
            while i < size:
                while i < size and s[i] == sub_str[0]:
                    sub_str += sub_str[0]
                    i += 1
                ans += (str(len(sub_str)) + sub_str[0])
                sub_str = []
                if i < size:
                    sub_str.append(s[i])
                    i += 1

            if sub_str:
                ans += (str(len(sub_str)) + sub_str[0])
            
            return ans


        s = '1'
        for i in range(n-1):
            s = read_it(s)

        return s
# @lc code=end

