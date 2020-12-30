/*
 * @lc app=leetcode.cn id=19 lang=java
 *
 * [19] 删除链表的倒数第N个节点
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // 一次遍历
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode first = dummy, second = dummy;
        int cnt = 0;
        while (cnt < n+1) {
            cnt++;
            first = first.next;
        }

        while (first != null) {
            second = second.next;
            first = first.next;
        }
        second.next = second.next.next;
        return dummy.next;

        // 两次遍历
        // ListNode dummy = new ListNode(0);
        // dummy.next = head;
        // int len = 0;
        // ListNode curr = head;
        // while (curr != null) {
        //     len++;
        //     curr = curr.next;
        // }
        // len -= n;
        // curr = dummy;
        // while (len > 0) {
        //     len--;
        //     curr = curr.next;
        // }
        // curr.next = curr.next.next;
        // return dummy.next;
    }
}
// @lc code=end

