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
    ListNode* removeElements(ListNode* head, int val) {
        //setting the start of the new chain
        ListNode* new_chain = head;
        while(new_chain != nullptr && new_chain -> val == val){
            new_chain = new_chain -> next;
            head = head -> next;
        }
        
        ListNode* prev = new_chain;
        while(head != nullptr && head->next != nullptr){
            if(head -> next -> val != val){
                ListNode* curr = head -> next;
                prev -> next = curr;
                prev = curr;
            }
            head = head -> next;
        }
        if(prev != nullptr)
        prev -> next = nullptr;
        return new_chain;
        
    }
};