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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1 == nullptr) return l2;
        if(l2 == nullptr) return l1;
                
        ListNode* prev;
        ListNode* start;
        if(l1 -> val > l2 -> val){
            //l2 goes first
            prev = new ListNode(l2 -> val);
            l2 = l2 -> next;
        } else{
            //l1 goes first
            prev = new ListNode(l1 -> val);
            l1 = l1 -> next;
        }
        start = prev;
        
        while(l1 != nullptr && l2 != nullptr){
            ListNode* curr = new ListNode();
            if(l1 -> val < l2 -> val){
                curr -> val = l1 -> val;
                l1 = l1 -> next;
            } else {
                curr -> val = l2 -> val;
                l2 = l2 -> next;
            }
            prev -> next = curr;
            prev = prev -> next;
        }
        
        if(l1 == nullptr && l2 != nullptr){
            prev -> next = l2;
        }
        if(l2 == nullptr && l1 != nullptr){
            prev -> next = l1;
        }
        return start;
    }
};