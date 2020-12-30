/*
 * @lc app=leetcode.cn id=12 lang=java
 *
 * [12] 整数转罗马数字
 */

// @lc code=start
class Solution {
    public String intToRoman(int num) {
        // 硬编码
        String[] thousands = new String[]{"","M","MM","MMM"};
        String[] hundreds = new String[]{"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
        String[] tens = new String[]{"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
        String[] ones = new String[]{"","I","II","III","IV","V","VI","VII","VIII","IX"};

        return thousands[num / 1000] + hundreds[num % 1000 / 100] + tens[num % 100 / 10] + ones[num % 10];

        // 贪心
        // int[] d = new int[]{1000,900,500,400,100,90,50,40,10,9,5,4,1};
        // String[] r = new String[]{"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

        // String ans = "";
        // int i = 0;
        // while (num > 0) {
        //     while (num < d[i]) i++;
        //     ans += r[i];
        //     num -= d[i];
        // }

        // return ans;
    }
}
// @lc code=end

