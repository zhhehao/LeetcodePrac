#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add_b(n1, n2, n3):
            if n3 == '0':
                if n1 == '1' and n2 == '1':
                    return ('0', '1')
                elif n1 == '0' and n2 == '0':
                    return ('0', '0')
                else:
                    return ('1', '0')
            else:
                if n1 == '1' and n2 == '1':
                    return ('1', '1')
                elif n1 == '0' and n2 == '0':
                    return ('1', '0')
                else:
                    return ('0', '1')

        m, n = len(a), len(b)
        i, j = m-1, n-1
        ans = ''
        up = '0'

        while i >= 0 or j >= 0:
            if i < 0:
                value, up = add_b('0', b[j], up)
                j -= 1
            elif j < 0:
                value, up = add_b(a[i], '0', up)
                i -= 1
            else:
                value, up = add_b(a[i], b[j], up)
                i -= 1
                j -= 1
            ans = value + ans

        if up == '1':
            ans = up + ans
        return ans

# @lc code=end

