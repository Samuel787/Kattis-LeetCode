/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }        
        ListNode headRef = new ListNode(-101);
        headRef.next = head;
        ListNode curr = head.next;
        ListNode prev = head;
        ListNode prevprev = headRef;
        while (curr != null) {
            if (curr.val == prev.val) {
                // remove all duplicates
                while (curr != null && curr.val == prev.val) {
                    prev.next = curr.next;
                    curr = curr.next;
                }
                // curr is null OR curr has diff val
                prevprev.next = curr;
                prev = curr;
                if (curr != null) {
                    curr = curr.next;
                }
            } else {
                prevprev = prev;
                prev = curr;
                curr = curr.next;
            }
        }
        return headRef.next;
    }
}