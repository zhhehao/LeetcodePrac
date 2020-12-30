/*
 * @lc app=leetcode.cn id=2 lang=java
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return getSum(l1, l2, 0);
    }

    private ListNode getSum(ListNode l1, ListNode l2, int ext) {
        if (l1 == null && l2 == null) {
            if (ext == 0) return null;
            else {
                return new ListNode(ext);
            }
        }
        if (l1 == null) {
            if (ext == 0) return l2;
            else {
                ListNode ret = new ListNode((l2.val + ext) % 10);
                ret.next = getSum(null, l2.next, (l2.val + ext)/10);
                return ret;
            }
        } else if(l2 == null) {
            if (ext == 0) return l1;
            else {
                ListNode ret = new ListNode((l1.val + ext) % 10);
                ret.next = getSum(l1.next, null, (l1.val + ext)/10);
                return ret;
            }
        } else {
            ListNode ret = new ListNode((l1.val + l2.val + ext) % 10);
            ret.next = getSum(l1.next, l2.next, (l1.val + l2.val + ext)/10);
            return ret;
        }
    }
}
// @lc code=end

