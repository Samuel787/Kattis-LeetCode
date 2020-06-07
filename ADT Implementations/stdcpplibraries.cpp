#include <bits/stdc++.h>
using namespace std;

//testing struct
struct Samuel{
    int iq = 120;
    int eq;
    string hobby;
};

int main(){
    //using map to count freq of letter S in a string
    string x = "I am Suther David Samuel";
    map<char, int> count;
    for(char c : x){
        count[c]++;
    }
    cout << count['S'] << endl;

    //inserting data into map using pairs
    map<string, int> map_of_words;
    map_of_words.insert(make_pair("earth", 1));
    map_of_words.insert(make_pair("fire", 2));
    map_of_words.insert(make_pair("water", 1));
    map_of_words.insert(make_pair("air", 3));

    cout << map_of_words["air"] << endl;
}