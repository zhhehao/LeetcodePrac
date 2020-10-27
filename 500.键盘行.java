import java.util.ArrayList;
import java.util.Collection;
import java.util.LinkedList;
import java.util.Set;

/*
 * @lc app=leetcode.cn id=500 lang=java
 *
 * [500] 键盘行
 */

// @lc code=start
class Solution {
    public String[] findWords(String[] words) {
        Set<Character> s1 = new HashSet<>();
        s1.add('q');
        s1.add('w');
        s1.add('e');
        s1.add('r');
        s1.add('t');
        s1.add('y');
        s1.add('u');
        s1.add('i');
        s1.add('o');
        s1.add('p');
        Set<Character> s2 = new HashSet<>();
        s2.add('a');
        s2.add('s');
        s2.add('d');
        s2.add('f');
        s2.add('g');
        s2.add('h');
        s2.add('j');
        s2.add('k');
        s2.add('l');
        Set<Character> s3 = new HashSet<>();
        s3.add('z');
        s3.add('x');
        s3.add('c');
        s3.add('v');
        s3.add('b');
        s3.add('n');
        s3.add('m');

        ArrayList<String> ans = new ArrayList<>();

        for (String w: words) {
            String w2 = w.toLowerCase();
            if (s1.contains(w2.charAt(0))) {
                boolean f1 = true;
                for (char c: w2.toCharArray()) {
                    if (!s1.contains(c)) {
                        f1 = false;
                        break;
                    }
                }
                if (f1) ans.add(w);
            } else if (s2.contains(w2.charAt(0))) {
                boolean f2 = true;
                for (char c: w2.toCharArray()) {
                    if (!s2.contains(c)) {
                        f2 = false;
                        break;
                    }
                }
                if (f2) ans.add(w);
            } else if (s3.contains(w2.charAt(0))) {
                boolean f3 = true;
                for (char c: w2.toCharArray()) {
                    if (!s3.contains(c)) {
                        f3 = false;
                        break;
                    }
                }
                if (f3) ans.add(w);
            }
        }
        String[] rec = new String[ans.size()];
        ans.toArray(rec);
        return rec;
    }
}
// @lc code=end

