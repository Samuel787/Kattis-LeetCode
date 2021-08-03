/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode* reversedLinkList = reverseLinkedList(head);
        if (n == 1) {
            return reverseLinkedList(reversedLinkList -> next);
        }
        int counter = 1;
        ListNode* curr = reversedLinkList;
        while (curr != nullptr) {
            if (counter == n - 1) {
                curr -> next = curr -> next -> next;
                break;
            } else {
                curr = curr -> next;
                counter++;
            }
        }
        return reverseLinkedList(reversedLinkList);
    
    }
    
    ListNode* reverseLinkedList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* temp = nullptr;
        
        while (curr != nullptr) {
            temp = curr -> next;
            curr -> next = prev;
            prev = curr;
            curr = temp;
        }
        
        return prev;
    }
    
};