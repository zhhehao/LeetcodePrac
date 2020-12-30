#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from typing import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # s_len = len(s)
        # def back_track(word, pos, end):
        #     if pos == end:
        #         word_len = len(word)
        #         for i in range(s_len):
        #             if s_len - i < word_len:
        #                 break
        #             if word in s[i:]:
        #                 ans.add(s[i:].index(word) + i)
                                   
        #         return

        #     for i in range(pos, end):
        #         words[i], words[pos] = words[pos], words[i]
        #         temp = words[pos]
        #         word += temp
        #         back_track(word, pos + 1, end)
        #         words[i], words[pos] = words[pos], words[i]
        #         word = word[:len(word)-len(temp)]

        # ans = set()
        # back_track("", 0, len(words))
        # return list(ans)
        
        from collections import Counter
        if not s or not words: 
            return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word:
            return []
        words = Counter(words) # 统计“可迭代序列”中每个元素的出现的次数
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left + one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num:
                        res.append(left)
        
        return res

            
# @lc code=end

