class Solution {
public:
    
    vector<int> getRow(int rowIndex) {
        vector<int> row;
        row.push_back(1);
        if(rowIndex == 0){
            return row;
        }
        row.push_back(1);
        if(rowIndex == 1){
            return row;
        }
        int elements = 2;
        for(int i = 2; i <= rowIndex; i++){
            elements++;
            int first;
            int second;
            for(int col = 0; col < elements - 1; col++){
                if(col == 0){
                    row.insert(row.begin(), 1);
                    first = row[1];
                    second = row[2];
                } else {
                    row[col] = first + second;
                    first = second;
                    if(col != elements - 2)
                        second = row[col + 2];
                }
            }
        }
        return row;
    }
};