class MyHashSet {
public:
    /** Initialize your data structure here. */
    vector<int> arr;
    
    MyHashSet() {
        
    }
    
    void add(int key) {
        bool exists = false;
        for(int x : arr){
            if(x == key) {
                exists = true;
                break;
            }
        }
        if(!exists){
            arr.push_back(key);
        }
    }
    
    void remove(int key) {
        int index = -1;
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] == key){
                index = i;
            }
        }
        // remove that element from the array
        if(index != -1)
            arr.erase(arr.begin() + index);
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        for(int i = 0; i < arr.size(); i++){
            if(arr[i] == key) return true;
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */