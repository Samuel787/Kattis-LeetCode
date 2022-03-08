/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null){
            return false;
        }
        ListNode fast = head.next.next;
        ListNode slow = head;
        while (fast != null && slow != null) {
            if (fast == slow) {
                return true;
            }
            slow = slow.next;
            fast = fast.next;
            if (fast == null) {
                return false;
            }
            fast = fast.next;
        }
        return false;
    }
}