#include <bits/stdc++.h>
using namespace std;

vector<string> filter_sound(string recording){
    vector<string> sounds;
    string sound = "";
    int start = 0;
    int end = 0;
    for(int i = 0; i < recording.size(); i++){
        
        if(recording[i] == ' '){
            sound = recording.substr(start, i - start);
            sounds.push_back(sound);
            start = i+1;
        } else if(i == (recording.size() - 1)){
            sound = recording.substr(start, recording.length() - start);
            sounds.push_back(sound);
        }
    }
    return sounds;
}

int main(){
    int n;
    cin >> n;
    cin.ignore();
    while(n > 0){
        string recording;
        //getline(cin, recording);
        getline(cin, recording);

        string data;
        unordered_set<string> sounds;
        while(getline(cin, data)){
            if(data == "what does the fox say?")
                break;
            string sound = data.substr(data.find("goes")+5, data.size());
            sounds.insert(sound);
        }
        //process the data

        vector<string> recorded_sounds = filter_sound(recording);
        string fox_sound = "";
        for(int i = 0; i < recorded_sounds.size(); i++){
            if(sounds.find(recorded_sounds[i]) == sounds.end()){
                if(i ==  recorded_sounds.size() - 1)
                    fox_sound += recorded_sounds[i];
                else
                    fox_sound += recorded_sounds[i] + " ";
            }
        }
        cout << fox_sound << endl;
        n--;
    }
}