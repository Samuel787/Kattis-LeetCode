class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> distinctEmails;
        for(int i = 0; i < emails.size(); i++){
            string local = getLocal(emails[i]);
            string domain = getDomain(emails[i]);
            string email = local + "@" + domain;
            distinctEmails.insert(email);
        }
        int count = 0;
        for(string x : distinctEmails){
            count++;
        }
        return count;
    }
    
    string getDomain(string email){
        string domain = "";
        bool after = false;
        for(int i = 0; i < email.size(); i++){
            if(after){
                domain += email[i];
            } else if(email[i] == '@'){
                after = true;
            }
        }
        return domain;
    }
    
    string getLocal(string email){
        string local = "";
        for(int i = 0; i < email.size(); i++){
            if(email[i] == '@'){
                break;
            } else {
                if(email[i] == '.'){
                    continue;
                } else if(email[i] == '+'){
                    break;
                } else {
                    local += email[i];
                }
            }
        }
        return local;
    }
};