import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=13 lang=java
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
class Solution {
    public int romanToInt(String s) {
        int rev = 0;
        Map<String, Integer> m = new HashMap<>();
        m.put("I", 1);
        m.put("IV", 4);
        m.put("IX", 9);
        m.put("V", 5);
        m.put("X", 10);
        m.put("XL", 40);
        m.put("XC", 90);
        m.put("L", 50);
        m.put("C", 100);
        m.put("CD", 400);
        m.put("CM", 900);
        m.put("D", 500);
        m.put("M", 1000);

        for (int i = 0; i < s.length(); ) {
            if (i == s.length()-1 ) {
                rev += m.get(""+s.charAt(i));
                i++;
            } else if (m.containsKey(""+s.charAt(i)+s.charAt(i+1))) {
                rev += m.get(""+s.charAt(i)+s.charAt(i+1));
                i += 2;
            } else {
                rev += m.get(""+s.charAt(i));
                i++;
            }
        }

        return rev;






    //     int rev = 0;
    //     for (int i = 0; i < s.length(); ) {
    //         switch(s.charAt(i)) {
    //             case 'M':
    //                 rev += 1000;
    //                 i++;
    //                 break;
    //             case 'D':
    //                 rev += 500;
    //                 i++;
    //                 break;
    //             case 'L':
    //                 rev += 50;
    //                 i++;
    //                 break;
    //             case 'V':
    //                 rev += 5;
    //                 i++;
    //                 break;
    //             case 'C':
    //                 if (i == s.length()-1 || (s.charAt(i+1) != 'D' && s.charAt(i+1) != 'M')) {
    //                     rev += 100;
    //                     i++;
    //                 } else if (s.charAt(i+1) == 'D' ) {
    //                     rev += 400;
    //                     i += 2;
    //                 } else if (s.charAt(i+1) == 'M') {
    //                     rev += 900;
    //                     i += 2;
    //                 }
    //                 break;
    //             case 'X':
    //                 if (i == s.length()-1 || (s.charAt(i+1) != 'L' && s.charAt(i+1) != 'C')) {
    //                     rev += 10;
    //                     i++;
    //                 } else if (s.charAt(i+1) == 'L' ) {
    //                     rev += 40;
    //                     i += 2;
    //                 } else if (s.charAt(i+1) == 'C') {
    //                     rev += 90;
    //                     i += 2;
    //                 }
    //                 break;
    //             case 'I':
    //                 if (i == s.length()-1) {
    //                     rev += 1;
    //                     i++;
    //                 } else if (i == s.length()-2) {
    //                     if (s.charAt(i+1) == 'I') {
    //                         rev += 2;
    //                         i += 2;
    //                     } else if (s.charAt(i+1) == 'V') {
    //                         rev += 4;
    //                         i += 2;
    //                     } else if (s.charAt(i+1) == 'X') {
    //                         rev += 9;
    //                         i += 2;
    //                     } else {
    //                         rev += 1;
    //                         i++;
    //                     }
    //                 } else {
    //                     if (s.charAt(i+1) == 'I' && s.charAt(i+2) == 'I') {
    //                         rev += 3;
    //                         i += 3;
    //                     } else if (s.charAt(i+1) == 'V') {
    //                         rev += 4;
    //                         i += 2;
    //                     } else if (s.charAt(i+1) == 'X') {
    //                         rev += 9;
    //                         i += 2;
    //                     } else {
    //                         rev += 1;
    //                         i++;
    //                     }
    //                 }
    //                 break;
    //         }
    //     }
    //     return rev;
    }
    
}
// @lc code=end

