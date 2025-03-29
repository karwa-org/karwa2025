/*
 * @EXPECTED_RESULTS@: WRONG-ANSWER
 */
#include<bits/stdc++.h>

using namespace std;

const int INF = numeric_limits<int>::max()/2;

int girth(vector<vector<int>>& adj, int current, int target, int parent, vector<int>& d) {

    if(parent != -1) d[current] = d[parent] + 1;

    int ans = INF;

    for(auto& v : adj[current]) {
        if(d[v] != INF){
            if(v == target &&  current != target) {
                return d[current]+1;
            }
            continue;
        }
        int out = girth(adj, v, target, current, d);
        ans = min(ans, out);
    }
    return ans;
}

void solve() {
    int n, m, p; cin >> n >> m >> p;
    vector<vector<int>> adj(n);
    vector<int> candidates(m);
    for(auto& i : candidates) cin >> i;

    for(int i = 0; i < p; i++) {
        int u, v; cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int ans = INF;
    for(auto& c : candidates) {
        vector<int> distances(adj.size(), INF);
        distances[c] = 0;
        ans = min(ans, girth(adj, c, c, -1, distances));
    }

    cout << ans << endl;

}

signed main() {
    solve();
    return 0;
}