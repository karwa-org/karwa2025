#include<bits/stdc++.h>

using namespace std;

const int INF = numeric_limits<int>::max()/2;

int girth(vector<vector<int>>& adj, int source) {
    vector<int> d(adj.size(), INF);
    d[source] = 0;
    queue<int> q;
    q.push(source);

    int shortest_cycle = INF;

    while(!q.empty()){
        int current = q.front(); q.pop();
        for(auto& v : adj[current]) {
            if(v == current) continue;
            if(d[v] == INF){
                d[v] = d[current] + 1;
                q.push(v);
            }else {
                shortest_cycle = min(shortest_cycle, d[current] + d[v] + 1);
                continue;
            }
        }
    }

    return shortest_cycle;
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
    int best_idx = -1;
    for(auto& c : candidates) {
        int g =  girth(adj, c);
        if (g < ans) {
            ans = g;
            best_idx = c;
        }
    }

    cout << best_idx << endl;

}

signed main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}