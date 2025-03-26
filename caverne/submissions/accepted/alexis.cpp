#include <stdio.h>
#include <ostream>
#include <iostream>
#include <math.h>
#include <cassert>
#include <vector>

#define int long long
#define double long double

using namespace std;

void solve() {
    int h, l, p; cin >> h >> l >> p;
    vector<vector<int>> mat1(l, vector<int>(p));
    vector<vector<int>> mat2(l, vector<int>(p));

    for(auto& i : mat1) {
        for(auto& k : i) cin >> k;
    }

    for(auto& i : mat2) {
        for(auto& k : i) cin >> k;
    }

    int ans = 0;
    for(int i = 0; i < l; i++) {
        for(int j = 0; j < p; j++ ) {
            ans += max((int)0, h-mat1[i][j]-mat2[i][j]);
        }
    }

    cout << ans << endl;
}

signed main() {
    solve();
    return 0;
}