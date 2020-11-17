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
        vector<int> number1;
        vector<int> number2;
        ListNode* l1_pointer = l1;
        while(l1 != nullptr){
            number1.push_back(l1 -> val);
            l1 = l1 -> next;
        }
        ListNode* l2_pointer = l2;
        while(l2 != nullptr){
            number2.push_back(l2 -> val);
            l2 = l2 -> next;
        }
        // int num1 = 0;
        // for(int i = 0; i < number1.size(); i++){
        //     num1 += number1[i] * pow(10, number1.size() - i - 1);
        // }
        // int num2 = 0;
        // for(int i = 0; i < number2.size(); i++){
        //     num2 += number2[i] * pow(10, number2.size() - i - 1);
        // }
        // int result = num1 + num2;
        // vector<int> reverse_digits;
        // do{
        //     reverse_digits.push_back(result % 10);
        //     result /= 10;
        // } while(result > 0);
        vector<int> reverse_digits = add_two_numbers(number1, number2);
        ListNode* prev = new ListNode(reverse_digits[0]);
        prev -> next = nullptr;
        for(int i = 1; i < reverse_digits.size(); i++){
            ListNode* curr = new ListNode(reverse_digits[i]);
            curr -> next = prev;
            prev = curr;
        }
        return prev;
    }
    
    vector<int> add_two_numbers(vector<int> a, vector<int> b){
        int length1 = a.size();
        int length2 = b.size();
        vector<int> temp;
        if(a.size() < b.size()){
            temp = a;
            a = b;
            b = temp;
        }
        //guaranteed that vector a is larger or same size
        vector<int> result;
        int carry = 0;
        for(int i = 0; i < b.size(); i++){
            int sum = a[a.size() - i - 1] + b[b.size() - i - 1];
            sum += carry;
            if(sum > 9){
                carry = 1;
                sum %= 10;
            } else {
                carry = 0;
            }
            result.push_back(sum);
        }
        for(int i = 0; i < (a.size() - b.size()); i++){
            int sum = a[a.size() - b.size() - i - 1] + carry;
            if(sum > 9){
                carry = 1;
                sum %= 10;
            } else {
                carry = 0;
            }
            result.push_back(sum);
        }
        if(carry == 1){
            result.push_back(1);
        }
        print_vector(result);
        return result;
    }
    
    void print_vector(vector<int> x){
        for(int a: x){
            cout << a << " ";
        }
        cout << endl;
    }
};