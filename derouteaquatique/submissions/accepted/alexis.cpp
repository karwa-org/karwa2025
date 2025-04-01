#include <stdio.h>
#include <ostream>
#include <iostream>
#include <math.h>
#include <cassert>
#include <vector>
#include <functional>
#include <iostream>
#include <queue>
#include <string_view>
#include <vector>

#define int long long
#define double long double

using namespace std;

const int INF = numeric_limits<int>::max()/2;

typedef struct  {
    pair<int, int> pos;
    int cost;
    bool in_pertubated;
} state_t;

void solve() {
    int n, m; cin >> n >> m;
    pair<int, int> start, end;
    cin >> start.first >> start.second;
    cin >> end.first >> end.second;

    
    vector<string> grid(n);
    for(auto&i : grid) {
        cin >> i;
    }

    auto cmp = [](state_t a, state_t b) {
        return a.cost > b.cost;
    };

    priority_queue<state_t, vector<state_t>, decltype(cmp)> pq(cmp);
    pq.push({
        start,
        0,
        false,
    });
    
    vector<vector<int>> dist(n, vector<int>(m, INF));

    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    dist[start.first][start.second] = 0;

    while(!pq.empty()){
        auto current = pq.top(); pq.pop();
        for(auto& d : dirs) {
            int nx = current.pos.first + d.first;
            int ny = current.pos.second + d.second;

            if(nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            

            int cc = 1;
            bool new_pertubation = current.in_pertubated;
            if (grid[current.pos.first][current.pos.second] == 'P') cc = 4;
            
            if(current.cost + cc < dist[nx][ny] ) {
                dist[nx][ny] = current.cost + cc;
                pq.push({
                    make_pair(nx, ny),
                    dist[nx][ny],
                    new_pertubation,
                });
            }
        }
    }

    cout << dist[end.first][end.second] << endl;
}

signed main() {
    solve();
    return 0;
}