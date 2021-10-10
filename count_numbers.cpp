#include<bits/stdc++.h>
using namespace std;

void print_vector(vector<long long> v) {
    cout << "This is vector: ";
    for(int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;
}
vector<long long> solve (int N, int Q, vector<int> X, vector<int> queries) {
   vector<long long> ans(Q);
   map<long, long> mPlot;
   for (int i = 0; i < X.size(); i++) {
      mPlot[X[i]]++;
   }
   for (int i = 0; i < Q; i++) {
      int query = queries[i];
      cout << "query" << query << endl;
      if (mPlot.find(query) != mPlot.end()) {
         ans[i] = mPlot[query];
      } else {
         int left = -1;
         int right = -1;
         int x = 0;
         int y = 0;
         auto itRight = mPlot.lower_bound(query);
         auto itLeft = mPlot.upper_bound(query);
         if (itRight != mPlot.end()) {
            y = (*itRight).second;
         }
         if (itLeft != mPlot.end()) {
            x = (*itLeft).second;
         }
         ans[i] = max(x,y);
        //  for (auto& it: mPlot) {
        //      cout << "it.first: " << it.first << " it.second" << it.second << endl;
        //     if (it.first < query) {
        //         cout << "it first is less than query" << endl;
        //        if (left == -1 || left < it.first) {
        //           left = it.first;
        //           x = it.second;
        //        }
        //     }
        //     if (it.first > query) {
        //        if (right == -1 || right > it.first) {
        //           right = it.first;
        //           y = it.second;
        //        }
        //     }
        //     cout << "x: " << x << " y:"  << y << endl;
        //  }         
         ans[i] = max(x, y);
      }
   }
   return ans;
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    cin >> N;
    int Q;
    cin >> Q;
    vector<int> X(N);
    for(int i_X = 0; i_X < N; i_X++)
    {
    	cin >> X[i_X];
    }
    vector<int> queries(Q);
    for(int i_queries = 0; i_queries < Q; i_queries++)
    {
    	cin >> queries[i_queries];
    }

    vector<long long> out_;
    out_ = solve(N, Q, X, queries);
    for (int i = 0; i < out_.size(); i++) {
       cout << out_[i] << endl;
    }
   //  cout << out_[0];
   //  for(int i_out_ = 1; i_out_ < out_.size(); i_out_++)
   //  {
   //  	cout << endl << out_[i_out_];
   //  }
}