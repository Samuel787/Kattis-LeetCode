class Solution {
public:
    int trap(vector<int>& height) {
        //idea, at each index, calculate the water level.
        vector<int> water_level;
        int total_volume = 0;
        for(int i = 0; i < height.size(); i++){
            if(i == 0 || i == height.size() - 1){
                total_volume += 0;
            } else {
                int max_left = height[i-1];
                int max_right = height[i+1];
                for(int j = i-1; j >= 0; j--){
                    if(height[j] > max_left){
                        max_left = height[j];
                    }
                }
                for(int j = i+1; j < height.size(); j++){
                    if(height[j] > max_right){
                        max_right = height[j];
                    }
                }
                int equilibrium_height = min(max_left, max_right);
                if(equilibrium_height > height[i])
                    total_volume += equilibrium_height - height[i];
            }
        }
        return total_volume;
    }
};