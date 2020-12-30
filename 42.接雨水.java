import jdk.nashorn.internal.runtime.linker.BoundCallable;

/*
 * @lc app=leetcode.cn id=42 lang=java
 *
 * [42] 接雨水
 */

// @lc code=start
class Solution {
    public int trap(int[] height) {
        // 双指针
        int left = 0, right = height.length - 1;
        int ans = 0;
        int left_max = 0, right_max = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= left_max) left_max = height[left];
                else ans += (left_max - height[left]);
                left++;
            } else {
                if (height[right] >= right_max) right_max = height[right];
                else ans += (right_max - height[right]);
                right--;
            }
        }

        return ans;

        // Stack
        // int ans = 0, cur = 0;
        // Stack<Integer> stack = new Stack<>();
        // while (cur < height.length) {
        //     while (!stack.empty() && height[cur] > height[stack.peek()]) {
        //         int top = stack.peek();
        //         stack.pop();
        //         if (stack.empty()) break;
        //         int distance = cur - stack.peek() - 1;
        //         int bounded_height = Math.min(height[cur], height[stack.peek()]) - height[top];
        //         ans += distance * bounded_height;
        //     }
        //     stack.push(cur++);
        // }
        // return ans;



        // 动态编程
        // if (height.length == 0) return 0;
        // int ans = 0;
        // int[] left_max = new int[height.length];
        // int[] right_max = new int[height.length];
        // left_max[0] = height[0];
        // for (int i = 1; i < height.length; i++) {
        //     left_max[i] = Math.max(left_max[i-1], height[i]);
        // }
        // right_max[height.length - 1] = height[height.length - 1];
        // for (int i = height.length - 2; i >= 0; i--) {
        //     right_max[i] = Math.max(right_max[i+1], height[i]);
        // }
        // for (int i = 1; i < height.length - 1; i++) {
        //     ans += Math.min(left_max[i], right_max[i]) - height[i];
        // }
        // return ans;

        // Brute
        // int ans = 0;
        // for (int i = 1; i < height.length; i++) {
        //     int left = 0, right = 0;
        //     for (int j = i; j >= 0; j--) {
        //         left = Math.max(left, height[j]);
        //     }
        //     for (int j = i; j < height.length; j++) {
        //         right = Math.max(right, height[j]);
        //     }
        //     ans += Math.min(left, right) - height[i];
        // }
        // return ans;
    }
}
// @lc code=end

