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
#include <algorithm>

#define int long long
#define double long double

using namespace std;

const int INF = numeric_limits<int>::max()/2;
#define EPSILON 1e-4

typedef struct {
    int idx;
    double x;
    double y;
    int deg;
} karwa_t;

karwa_t rotate_point(karwa_t pt, int deg) {
    double rad = (double)deg * M_PI / 180.0;
    double c_theta = cos(rad);
    double s_theta = sin(rad);

    double new_x = c_theta * pt.x - s_theta * pt.y;
    double new_y = s_theta * pt.y - c_theta * pt.x;

    int new_deg = (pt.deg + deg)%360;
    return {pt.idx, new_x, new_y, new_deg};
}

//TODO UN TESTE OÙ ILS POINTENT TOUS DANS LA MÊME DIRECTION ET ILS SONT ALLIGÉS
//POUR CASSER LE SWEEP LINE A 2 PASS
void solve() {
    int n; cin >> n;
    vector<karwa_t> karwa(n);

    for(int i = 0; i < n; i++) {
        cin >> karwa[i].x >> karwa[i].y >> karwa[i].deg;
        karwa[i].idx = i;
    }

    int fish; cin >> fish;

    // Our graph :)
    vector<vector<int>> adj(n); 

    // Rotate the plane at 360
    for(int rot = 0; rot < 360; rot++) {
        //perform the rotation of the plane 
        vector<karwa_t> new_points;
        for(auto& point : karwa) {
            new_points.push_back(rotate_point(point, rot));
        }
        
        // Sort by y and if same y (then collinear sort them by least x)
        sort(new_points.begin(), new_points.end(), [](karwa_t a, karwa_t b) {
            if((a.y -b.y) < EPSILON){
                return a.x < b.x;
            } else {
                return a.y > b.y;
            }
        });

        cerr << "rotation : " << rot <<  " -  ";

        for(auto& p : new_points){
            cerr << "( " << p.x << " "  << p.y << ")" << ", ";
        }
        cerr << endl;

        // Now a sweep line and construct the graph
        for(int j = 0; j < n-1; j++) {
            if (new_points[j].deg != 0) continue;
            cerr << "wtf" << endl;
            if((new_points[j].y - new_points[j+1].y) < EPSILON) {
                adj[new_points[j].idx].push_back(new_points[j+1].idx);
                adj[new_points[j+1].idx].push_back(new_points[j].idx);
            }
        }
    }

    for(int i = 0; i < n; i++) {
        cerr << "adj["<<i<<"] : ";
        for(auto& k : adj[i]) cerr << k << " ";
        cerr << endl;
    }

    // Now a bfs to find the size of the component
    queue<int> q;
    q.push(fish);
    vector<bool> visited (n, false);
    int ans = 0;
    while(!q.empty()){
        int current = q.front(); q.pop();
        ans ++;
        visited[current] = true;
        for(auto& k : adj[current]) {
            if(visited[k]) continue;
            q.push(k);
        }
    }
    cout << ans << endl;
    
}

signed main() {
    solve();
    return 0;
}