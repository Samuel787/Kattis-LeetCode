#include <bits/stdc++.h>
using namespace std;

struct data1{
    int first_day = 0;
    int second_day = 0;
    bool first_hit = false;
    bool second_hit = false;
};



string get_day(int day){
    day %= 7;
    switch(day){
        case 0:
            return "Saturday";
            break;
        case 1:
            return "Sunday";
            break;
        case 2:
            return "Monday";
            break;
        case 3: 
            return "Tuesday";
            break;
        case 4:
            return "Wednesday";
            break;
        case 5:
            return "Thursday";
            break;
        case 6:
            return "Friday";
            break;
        default:
            return "LOL";
    }
}

void format_time(int minutes){
    int hrs;
    int mins;
    hrs = minutes / 60;
    mins = minutes - hrs * 60;

    string hour, min;
    if(hrs < 10){
        hour = "0" + to_string(hrs);
    } else {
        hour = to_string(hrs);
    }
    if(mins < 10){
        min = "0" + to_string(mins);
    } else {
        min = to_string(mins);
    }
    string result = hour + ":" + min; 
    cout << result << endl;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    string first_star;
    string second_star;
    string first_freq;
    string second_freq;
    cin >> first_star;
    cin >> second_star;
    cin >> first_freq;
    cin >> second_freq;

    //checking the parsing of the data
    string ff = first_star.substr(0, first_star.find(":"));
    string fs = first_star.substr(first_star.find(":") + 1, first_star.length());
    
    string sf = second_star.substr(0, second_star.find(":"));
    string ss = second_star.substr(second_star.find(":") + 1, second_star.length());

    string fff = first_freq.substr(0, first_freq.find(":"));
    string ffs = first_freq.substr(first_freq.find(":") + 1, first_freq.length());

    string sff = second_freq.substr(0, second_freq.find(":"));
    string sfs = second_freq.substr(second_freq.find(":") + 1, second_freq.length());

    //a day has 1440 minutes -> parsing data into minutes
    int fs_timing = stoi(ff) * 60 + stoi(fs);
    int ss_timing = stoi(sf) * 60 + stoi (ss);

    int fs_freq = stoi(fff) * 60 + stoi(ffs);
    int ss_freq = stoi(sff) * 60 + stoi(sfs);

    //array with timings
    vector<data1> minutes;

    for(int i = 0; i < 1440; i++){
        minutes.push_back(data1());
    }

    int day = 0;
    
    //simulate the first star;
    while(minutes[fs_timing].first_hit == false){
        minutes[fs_timing].first_day = day;
        minutes[fs_timing].first_hit = true;
        fs_timing += fs_freq;
        if(fs_timing >= 1440){
             fs_timing %= 1440;
             day++;
        }
    }

    //simulate the second star;
    day = 0;
    while(minutes[ss_timing].second_hit == false){
        minutes[ss_timing].second_day = day;
        minutes[ss_timing].second_hit = true;
        ss_timing += ss_freq;
        if(ss_timing > 1440){
            ss_timing %= 1440;
            day++;
        }
    }

    //check if there's a hit
    bool is_hit = false;
    for(int i = 0; i < 1440; i ++){
        if(minutes[i].first_hit == true 
            && minutes[i].second_hit == true
             && (minutes[i].first_day == minutes[i].second_day
                // || minutes[i].first_day % minutes[i].second_day == 0
                // || minutes[i].second_day % minutes[i].first_day == 0
             )){
                 is_hit = true;
                 cout << get_day(minutes[i].first_day) << endl;   
                 format_time(i);
                 //break;
             }
    }

    if(!is_hit){
        cout << "Never" << endl;
    }
}
