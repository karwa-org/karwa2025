/*
 * Solution en O(m*p) avec un dfs
 * @EXPECTED_RESULTS@: WRONG-ANSWER
 */
#include<bits/stdc++.h>

using namespace std;

const int INF = numeric_limits<int>::max()/2;

int best_solution = INF;

int girth(vector<vector<int>>& adj, int current, int target, int parent, vector<int>& d) {
    int ans = INF;
    if (d[current] >= best_solution) {
        return d[current];
    }

    for(auto& v : adj[current]) {
        if(v == current) continue;
        if(d[v] != INF){
            if(v == target &&  current != target && parent != target) {
                return d[current]+1;
            }
            continue;
        }else{
            d[v] = d[current] + 1;
            int out = girth(adj, v, target, current, d);
            ans = min(ans, out);
        }

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

    int best_idx = -1;
    unordered_map<int, vector<int>> all_ans;

    for(auto& c : candidates) {
        vector<int> distances(adj.size(), INF);
        distances[c] = 0;
        int g = girth(adj, c, c, -1, distances);
        all_ans[g].push_back(c);
        if(g < best_solution) {
            best_solution = g;
            best_idx = c;
        }
    }

    cout << all_ans[best_solution].size() << endl;
    for(auto& k : all_ans[best_solution]){
        cout << k << " ";
    }
    cout << endl;

}

signed main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}