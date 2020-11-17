class RecentCounter {
public:
    vector<int> ping_timing;
    RecentCounter() {
        int counter = 0;
        int current_time = 0;
    }

    void add_ping(int t){
        ping_timing.push_back(t);
    }

    int num_requests_in_past_3000(int t){
        int counter = 0;
        for(int i = ping_timing.size() - 1; i >= 0; i--){
            if(ping_timing[i] >= t-3000){
                counter += 1;
            }
            if(ping_timing[i] < t-3000){
                break;
            }
        }
        return counter;
    }
    
    int ping(int t) {
        add_ping(t);
        return num_requests_in_past_3000(t);
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */