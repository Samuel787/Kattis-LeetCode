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
    ListNode* swapPairs(ListNode* head) {
        ListNode* temp = new ListNode(0);
        temp -> next = head;
        ListNode* current = temp;
        while(current -> next != nullptr && current -> next -> next != nullptr){
            ListNode* last = current -> next -> next -> next;
            ListNode* first = current -> next;
            ListNode* second = current -> next -> next;
            current -> next = second;
            second -> next = first;
            first -> next = last;
            current = current -> next -> next;
        }
        return temp -> next;
    }
};