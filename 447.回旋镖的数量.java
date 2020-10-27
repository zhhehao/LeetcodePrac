/*
 * @lc app=leetcode.cn id=447 lang=java
 *
 * [447] 回旋镖的数量
 */

// @lc code=start
class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int len = points.length;
        HashMap<Integer, HashMap<Integer, Integer>> m = new HashMap<>();
        for (int i = 0; i < len; i++) {
            m.put(i, new HashMap<Integer, Integer>());
        }
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (i != j) {
                    int dis = (points[i][0]-points[j][0]) * (points[i][0]-points[j][0]) +
                              (points[i][1]-points[j][1]) * (points[i][1]-points[j][1]);
                    HashMap<Integer, Integer> temp = m.get(i);
                    if (temp.containsKey(dis)) temp.put(dis, temp.get(dis)+1);
                    else temp.put(dis, 1);
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < len; i++) {
            HashMap<Integer, Integer> temp = m.get(i);
            for (int k: temp.keySet()) {
                int n = temp.get(k);
                if (n == 1) continue;
                ans += n * (n-1);
            }
        }

        return ans;

    }

}
// @lc code=end

