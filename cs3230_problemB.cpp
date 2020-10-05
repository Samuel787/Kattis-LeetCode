#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<long,long> ii;
 
vector<ii> v;
ll ans = LONG_LONG_MAX, sum = 0, n;
unordered_set<ll> val;
bool valid(ll m) {
    map<ll, ll> vis;
    queue<ll> q;
    int ptr = (int)(v.size()) - 1;
    q.push(m);
    ll ms = m;
    vis[m]++;
    while (!q.empty()) {
        ll u = q.front(), &lft = vis[u];
        q.pop();
        if (v[ptr].first == u) {
            if (v[ptr].second <= lft) {
                lft -= v[ptr].second;
            } else return false;
            ptr--;
            if (ptr < 0) return true;
            if (!lft) continue;
        } else if (v[ptr].first > u) return false;
        ll ub = (u >> 1), lb = (u >> 1);
        if ((ll)(lb << 1) != u) ub++;
        if (ms > ub) q.push(ub), ms = ub;
        if (ms > lb) q.push(lb), ms = lb;
        vis[ub] += lft, vis[lb] += lft;
    }
    return false;
}
 
void find(long m) {
    unordered_set<long> vis;
    queue<long> q;
    q.push(m);
    long ms = m;
    while (!q.empty()) {
        long u = q.front();
        val.insert(u);
        q.pop();
        long ub = (u >> 1), lb = (u >> 1);
        if ((long)(lb << 1) != u) ub++;
        if (ms > ub) q.push(ub), ms = ub;
        if (ms > lb) q.push(lb), ms = lb;
    }
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int t; cin >> t;
    //t = 2;
    cin >> n;
    map<long, int> m;
    if (t == 1) {
        ll amt; cin >> amt;
        for (int i = 0; i < n; i++) {
            long a; cin >> a;
            m[a]++;
        }
        for (auto &[key,val] : m) v.push_back({key,val});
        if (valid(amt)) {
            cout << "YES";
        } else cout << "NO";
    } else {
        for (int i = 0; i < n; i++) {
            long a; cin >> a;
            m[a]++;
        }
        for (auto &[key,val] : m) v.push_back({key,val}), sum += key * val;
        ll gre = v.back().first, qty = v.back().second;
        if (gre == 1) {
            cout << n;
        } else if (n == 1) {
            cout << gre;
        } else {
            find(gre), find(gre + 1), find(gre - 1);
            bool ac = true;
            for (ii &p : v) {
                if (!val.count(p.first)) {
                    ac = false; break;
                }
            }
            if (!ac) {
                cout << "IMPOSSIBLE";
                return 0;
            }
            ac = false;
            for (int z = 1; z <= 2 * n && !ac; z <<= 1) {
                for (ll i = (gre - 1) * z; i < (gre + 1) * z; ++i) {
                    if (i >= sum && valid(i)) {
                        ans = i; ac = true; break;
                    }
                }
            }
            if (ac) {
                cout << ans;
            } else cout << "IMPOSSIBLE";
        }
    }
}