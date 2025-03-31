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

typedef struct {
    int pos;
    int speed;
    int idx;
} fish_t;

void solve() {
    int n; cin >> n;
    vector<fish_t> a(n); 
    for(auto& i : a)  {
        cin >> i.pos;
    }
    for(auto& i : a) {
        cin >> i.speed;
    }
    for(int i = 0; i < n; i++) {
        a[i].idx = i;
    }

    int target; cin >> target;

    sort(a.begin(), a.end(), [](fish_t a, fish_t b) {
        return a.pos < b.pos;
    });

    int ans = 0;

    for(int i = 0; i < n-1; i++){
        fish_t ff = a[i+1];
        fish_t bb = a[i];
        
        //check if behind will overpass forward
        double collision = -1;
        if(bb.speed == ff.speed) {
            collision = INF;
        }else {
            collision = (ff.pos - bb.pos) / (double)(bb.speed - ff.speed);

        }
        
        double position = bb.speed * collision + bb.pos;
        double position2 = ff.speed * collision + ff.pos;
        
        if(position > target || collision < 0) {
            ans++;
        }
    }
    ans++;

    cout << ans << endl;

}

signed main() {
    solve();
    return 0;
}