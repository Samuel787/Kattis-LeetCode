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
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        
        while(fast != nullptr && fast->next != nullptr){
            fast = fast->next->next;
            slow = slow->next;
        }
        
        /*
            Reverse the right half of the linked list
        */
        ListNode* prev = nullptr; //initialize the new chain
        while(slow != nullptr){ 
            ListNode* next = slow->next; //get the remaining chain
            slow->next = prev; //break the chain and reverse the direction of the current node
            prev = slow; //set prev to current node
            slow = next; //update head to next node
        }
        
        slow = prev;
        fast = head;
        
        while(slow != nullptr){
            if(slow->val != fast->val){
               return false;
            } 
            slow = slow->next;
            fast = fast->next;
        }
        
        return true;
    }
};