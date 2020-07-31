#include <bits/stdc++.h>
using namespace std;

unordered_map<string, vector<string>> dp;

void print_vector(vector<string> input){
    for(string x : input){
        cout << x << ", ";
    } 
    cout << endl;
}

    
//     vector<string> wordBreak(string s, vector<string>& wordDict){
//         if(dp.find(s) != dp.end()) return dp[s];
//         vector<string> result;
        
//         for(string word : wordDict){
//             if(s.substr(0, word.size()) == word){
//                 if(s.size() == word.size()){
//                     result.push_back(word);
//                 } else {
//                     vector<string> temp = wordBreak(s.substr(word.size(), s.size()), wordDict);
//                     for(string x : temp){
//                         result.push_back(word + " " + x);
//                     }

//                 }
//             } 
//         }
//         dp[s] = result;
//         return result;
//     }
    
vector<string> wordBreak(string s, vector<string>& wordDict) {
    if(dp.find(s) != dp.end()) return dp[s];
    vector<string> results;
    for(string word: wordDict){
        if(s.size() < word.size()){
            continue;
        } else if(s == word){
            results.push_back(word);
        } else {
            if(s.substr(0, word.size()) == word){    
            vector<string> temp;
            temp = wordBreak(s.substr(word.size(), s.size()), wordDict); // all possible decompositions
            for(string x : temp){
                results.push_back(word + " " + x);
            }
            }
        }
    }
    dp[s] = results;
    return results;
}





/***
 *  RECURSIVE SOLUTION -> WORKS BUT TIME LIMIT EXCEED
 * 
void print_vector(vector<string> input){
    for(string x : input){
        cout << x << ", ";
    } 
    cout << endl;
}
vector<string> break_string(string s, vector<string>& wordDict, string sentence){
    vector<string> sentences;
    bool match = false;
    for(string x: wordDict){
        if(s == x){
            sentence += s;
            sentences.push_back(sentence);
            match = true;
        } else if(s.size() > x.size()){
            if(s.substr(0, x.size()) == x){
                //we found 1 match so we can recurse somemore
                string new_sentence = sentence + x + " ";
                cout << new_sentence << " is the new sentence" << endl;
                // guaranteed to have left over string
                vector<string> results = break_string(s.substr(x.size(), s.size()), wordDict, new_sentence);
                sentences.insert(end(sentences), begin(results), end(results));
            }
        } else {
            //size of word in dict is greater than the remaining string -> impossible
        }   
    }
    return sentences;
}

vector<string> wordBreak(string s, vector<string>& wordDict) {
    //sort the wordDict by size of strings
    sort(wordDict.begin(), wordDict.end());
    return break_string(s, wordDict, "");
}
*/


/**
 * Driver code
*/
int main(){
    string s = "catsanddog";
    vector<string> wordDict{"cat", "cats", "and", "sand", "dog"};
    print_vector(wordBreak(s, wordDict));
}