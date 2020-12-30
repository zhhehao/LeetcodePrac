/*
 * @lc app=leetcode.cn id=8 lang=java
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
class Solution {
    class Automaton {
        final String START = "start";
        final String SIGNED = "signed";
        final String IN_NUM = "in_number";
        final String END = "end";
        String state = START;
        Map<String, String[]> map;
        public int sign = 1;
        public long ans = 0;

        public Automaton(){
            map = new HashMap<>();
            map.put(START, new String[]{START, SIGNED, IN_NUM, END});
            map.put(SIGNED, new String[]{END, END, IN_NUM, END});
            map.put(IN_NUM, new String[]{END, END, IN_NUM, END});
            map.put(END, new String[]{END, END, END, END});
        }
    
        public int get_col(char c) {
            if (c == ' ') return 0;
            if (c == '+' || c == '-') return 1;
            if (c >= '0' && c <= '9') return 2;
            return 3;
        }
    
        public void get(char c) {
            state = map.get(state)[get_col(c)];
            if (state.equals(IN_NUM)) {
                ans = ans * 10 + c - '0';
                if (sign == 1) {
                    ans = Math.min(ans, Integer.MAX_VALUE);
                } else {
                    ans = Math.min(ans, -(long)Integer.MIN_VALUE);
                }
            } else if (state.equals(SIGNED)) 
                sign = c == '+' ? 1 : -1;
        }
    }

    

    public int myAtoi(String str) {
        // 自动机
        Automaton automaton = new Automaton();
        char[] c = str.toCharArray();
        for (char ch : c) {
            automaton.get(ch);
        }
        return automaton.sign * ((int) automaton.ans);
        // char[] ch = str.toCharArray();
        // int i = 0;
        // while (i < ch.length && ch[i] == ' ') i++;
        // if (i == ch.length) return 0;
        // if (!Character.isDigit(ch[i]) && ch[i] != '+' && ch[i] != '-') return 0;
        // int ans = 0;
        // if (ch[i] == '-') {
        //     i++;
        //     while (i < ch.length && Character.isDigit(ch[i])) {
        //         int n = (int)(ch[i]-'0') * -1;
        //         if ((Integer.MIN_VALUE - n) / 10 > ans) return Integer.MIN_VALUE;
        //         ans = ans * 10 + n;
        //         i++;
        //     }
        // } else {
        //     if (ch[i] == '+') i++;
        //     while (i < ch.length && Character.isDigit(ch[i])) {
        //         int n = (int)(ch[i]-'0');
        //         if ((Integer.MAX_VALUE - n) / 10 < ans) return Integer.MAX_VALUE;
        //         ans = ans * 10 + n;
        //         i++;
        //     }
        // }

        // return ans;
    }
}
// @lc code=end

