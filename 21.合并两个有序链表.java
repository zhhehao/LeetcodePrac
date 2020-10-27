/*
 * @lc app=leetcode.cn id=21 lang=java
 *
 * [21] 合并两个有序链表
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        ListNode rev = null;
        ListNode now = null;

        while (l1 != null || l2 != null) {
            if (l1 == null) {
                now.next = l2;
                break;
            } else if (l2 == null) {
                now.next = l1;
                break;
            } else {
                ListNode selectNode;
                if (l1.val <= l2.val) {
                    selectNode = l1;
                    l1 = l1.next;
                } else {
                    selectNode = l2;
                    l2 = l2.next;
                }
                if (rev == null) {
                    rev = selectNode;
                    now = rev;
                } else {
                    now.next = selectNode;
                    now = now.next;
                }
            }
        }

        return rev;
    }
}
// @lc code=end

