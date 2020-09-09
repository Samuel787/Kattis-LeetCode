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
    ListNode* partition(ListNode* head, int x) {
        ListNode* low = new ListNode();
        ListNode* low_start = low;
        ListNode* high = new ListNode();
        ListNode* high_start = high;
        
        while(head != nullptr){
            if(head -> val < x){
                low -> next = head;
                low = low -> next;
            } else {
                high -> next = head;
                high = high -> next;
            }
            head = head -> next;
        }
        high -> next = nullptr;
        low -> next = high_start -> next;
        return low_start -> next;
    }
};
