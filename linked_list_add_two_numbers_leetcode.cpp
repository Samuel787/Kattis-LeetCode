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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        // i think we have to do string addition 
        int carry = 0;
        ListNode* result = new ListNode();
        ListNode* head = result;
        while(l1 != nullptr && l2 != nullptr){
            int val1 = l1 -> val;
            int val2 = l2 -> val;
            int sum = val1 + val2 + carry;
            if(sum > 9){
                carry = 1;
                sum %= 10;
            } else {
                carry = 0; //reset carry 
            }
            
            ListNode* curr = new ListNode(sum);
            result -> next = curr;
            result = curr;
            l1 = l1 -> next;
            l2 = l2 -> next;
        }
        // one of them have become nullptrs
        while(l1 != nullptr){
            int sum = l1 -> val + carry;
            if(sum > 9){
                carry = 1;
                sum %= 10;
            } else {
                carry = 0; //reset carry
            }
            
            ListNode* curr = new ListNode(sum);
            result -> next = curr;
            result = curr;
            l1 = l1 -> next;
        }
        
                // one of them have become nullptrs
         while(l2 != nullptr){
            int sum = l2 -> val + carry;
            if(sum > 9){
                carry = 1;
                sum %= 10;
            } else {
                carry = 0; //reset carry
            }
            
            ListNode* curr = new ListNode(sum);
            result -> next = curr;
            result = curr;
            l2 = l2 -> next;
        }
        
        // both of them have become nullptrs
        if(carry == 1){
            result -> next = new ListNode(1);
            result = result -> next;
        }
        result -> next = nullptr;
        return head -> next;
    }
};