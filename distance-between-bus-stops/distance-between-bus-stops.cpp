class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        
        int fwdDist = 0;
        int bwdDist = 0;
        int size = distance.size();
        
        int startIndex = start;
        while (startIndex != destination) {
            fwdDist += distance[startIndex];
            startIndex++;
            startIndex %= size;
        }
        
        startIndex= start;
        while (startIndex != destination) {
            startIndex--;
            if (startIndex < 0) {
                startIndex = size - 1;
            }
            bwdDist += distance[startIndex];
        }
        
        return fwdDist > bwdDist ? bwdDist : fwdDist;
        
    }
};