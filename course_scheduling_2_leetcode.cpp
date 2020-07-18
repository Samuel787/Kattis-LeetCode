class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> ans;
        vector<vector<int>> graph;
        for(int i = 0; i < numCourses; i++){
            vector<int> prereqs;
            graph.push_back(prereqs);
        }
        for(int i = 0; i < prerequisites.size(); i++){
            vector<int> prereq = prerequisites[i];
            graph[prereq[0]].push_back(prereq[1]);
        }
        while(ans.size() != numCourses){
            //get the course with the fewest prereqs
            int courseID = -1;
            for(int i = 0; i < graph.size(); i++){
                if(graph[i].size() == 0){
                    courseID = i;
                    graph[i].push_back(-1); //so that size is not 0
                    
                    //update the graph
                    for(int i = 0; i < graph.size(); i++){
                        for(int j = 0; j < graph[i].size(); j++){
                            if(graph[i][j] == courseID){
                                graph[i].erase(graph[i].begin() + j);
                            }
                        }
                    }
                    break;
                }
            }
            //find a course with all prereqs completed
            // if 0
            if(courseID != -1){
                //then complete this course -> remove it from graph prereqs
                ans.push_back(courseID);
                // find the next course with 0 prereqs
            }
            else{
                vector<int> new_ans;
                return new_ans;
            }
            //else
                // no course with 0 prereqs exist -> impossible
        }
        return ans;
    }
};